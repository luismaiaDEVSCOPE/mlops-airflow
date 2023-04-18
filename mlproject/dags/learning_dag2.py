
from __future__ import annotations
import sys, os
import datetime
from airflow.models import DAG

# import airflow.providers.papermill.operators.papermill as afl_pml
# from airflow.providers.papermill.operators.papermill import PapermillOperator
from airflow.operators.python_operator import PythonVirtualenvOperator, PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from airflow.decorators import dag, task



# Add root source to PATH
MLPROJECT = '/opt/airflow' # TODO: check if the folder path needs to be read from somewhere else
sys.path.append(MLPROJECT)

# from engine.helpers import connections
# import utils
# from datetime import date

args = {
    'depends_on_past': False,
    'email': ['youemail@mail.net'],
    'email_on_failure': False,
    'email_on_retry': False,
    'owner': 'DevScope',
    'start_date': datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0),
    'provide_context': True,
    'retries': 3,
    'retry_delay': datetime.timedelta(minutes=1),
    'catchup': False
}

# with DAG(
#     'learning_worflow',
#     schedule_interval="@daily",
#     default_args=args
# ) as dag :

@dag(schedule_interval="2 * * * *", #"@daily",
    start_date=datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0),
    catchup=False,
    tags=["learn precedence and return statements"],
    )

def learning_worflow2() :

    @task
    def extract_data_function(value) :
        if value :
            data = [*range(1,11)] 
            print(data)

            return data

        return []

    @task
    def transform_data_function(data: list, value) :
        if value :

            print(" in: %s" % (str(data)))
            data = [i*2 for i in data]
        
            print("out: %s" % (str(data)))
            return data

        return []

    @task
    def load_data_function(data: list, data2: list) :
        print(data)
        print(data2)

        with open("/opt/airflow/vals.txt", "w") as f :
            for i in data :
                f.write(f"{i}\n")

        assert os.path.exists("/opt/airflow/vals.txt")


    @task
    def check_db_connect() :
        from sqlalchemy import create_engine
        from sqlalchemy.engine import URL

        # Using db from https://rnacentral.org/help/public-database
        url_object = URL.create('postgresql+psycopg2', 
            username='reader', password='NWDMCE5xdipIjRrp', 
            host='hh-pgsql-public.ebi.ac.uk', port='5432', 
            database='pfmegrnargs')

        with create_engine(url_object).connect() as conn :
            res = conn.execute('SELECT upi, len, md5, timestamp FROM Rna fetch first 5 rows only;')
            print(res.fetchall())
    

    @task
    def get_dependency() :
        return True

    # definition

    dep = get_dependency()

    data = extract_data_function(dep)
    data_trans = transform_data_function([*range(10, 110, 10)], dep)


    load_data_function(data_trans, data)
    check_db_connect()

    # end_node = DummyOperator(task_id='workflow_finish', dag=dag)

    # def create_graph() :
    #     # start - get data for predictions from db - predict - save preds in db - end
    #     start_node >> end_node

    # create_graph()

learning_worflow2()