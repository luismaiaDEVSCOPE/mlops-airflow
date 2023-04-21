from __future__ import annotations

import os
import datetime
# from airflow.models import DAG

# pip install apache-airflow-providers-papermil was missing # USED .env file

from airflow.providers.papermill.operators.papermill import PapermillOperator
#from airflow.operators.python import PythonVirtualenvOperator
from airflow.operators.python_operator import PythonVirtualenvOperator, PythonOperator
# from airflow.operators.dummy_operator import DummyOperator
# from airflow.operators.bash_operator import BashOperator
from airflow.decorators import dag, task
from airflow.sensors.python import PythonSensor

args = {
    'depends_on_past': False,
    # 'email': ['youemail@mail.net'],
    'email_on_failure': False,
    'email_on_retry': False,
    'owner': 'DevScope',
    'start_date': datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0),
    'provide_context': True,
    'retries': 3,
    'retry_delay': datetime.timedelta(minutes=1),
    'catchup': False,
    'dagbag_import_timeout': 600
}

@dag(schedule_interval="2 * * * *", #"@daily",
    start_date=datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0),
    catchup=False,
    # tags=[""],
    default_args=args
    )

def inference_worflow() :

    @task()
    def get_dev_data() :
        return "yay"

    @task()
    def inference(test_set) :
        import pandas as pd
        import numpy as np
        import mlflow

        test_set = pd.read_parquet('/opt/airflow/datasets/absenteeism/test_set.parquet')
        test_set.convert_dtypes()
        test_set.reset_index(drop=True, inplace=True)

        # /opt/airflow/modelscurrent/a7f818f9ad574747b3763c95d0274b4d/artifacts/model\MLmodel

        logged_model = '/opt/airflow/datasets/models/current/a7f818f9ad574747b3763c95d0274b4d/artifacts/model/'
        import os
        assert os.path.exists(logged_model)
        loaded_model = mlflow.sklearn.load_model(logged_model)

        cols_path = '/opt/airflow/datasets/models/current/a7f818f9ad574747b3763c95d0274b4d/artifacts/columns/columns.json'

        if os.path.exists(cols_path) :
            import json
            json_str = ''
            cols = []
            with open(cols_path, 'r') as f :
                json_str=f.read()
            
            cols = json.loads(json_str)
            test_set_small = test_set[cols]
        else :
            test_set_small = test_set

        
        pred_probs = loaded_model.predict_proba(test_set_small)
        res = np.zeros(((2, len(pred_probs))))

        res[0] = np.amax(pred_probs, axis=1)
        res[1] = np.argmax(pred_probs, axis=1)

        probs_df = pd.DataFrame(data=np.rot90(res), columns=["Probabilty", "State"])
        del res
        print(probs_df)
        # pd.concat([df1, df4], axis=1)
        # probs_df.to_csv('/opt/airflow/results/probabilitys.csv', index=False)

    inference(get_dev_data())

# inference_worflow()