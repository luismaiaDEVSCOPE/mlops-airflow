
from __future__ import annotations
import sys, os
import datetime
from airflow.models import DAG

# pip install apache-airflow-providers-papermil was missing

from  airflow.providers.papermill.operators.papermill import PapermillOperator
# from airflow.operators.papermill_operator import PapermillOperator
from airflow.operators.python_operator import PythonVirtualenvOperator, PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from airflow.decorators import dag, task
from airflow.sensors.python import PythonSensor

from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import pandas as pd
import papermill as pm

# Using db from https://rnacentral.org/help/public-database
url_object = URL.create('postgresql+psycopg2', 
    username='reader', password='NWDMCE5xdipIjRrp', 
    host='hh-pgsql-public.ebi.ac.uk', port='5432', 
    database='pfmegrnargs')

def run_db_statement(statement) :
    with create_engine(url_object).connect() as conn :
        res = conn.execute(statement)
        yield pd.DataFrame(res.fetchall(), columns=res.keys())

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
    'catchup': False,
    'dagbag_import_timeout': 600
}

@dag(schedule_interval="2 * * * *", #"@daily",
    start_date=datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0),
    catchup=False,
    tags=["prepro"],
    default_args=args
    )

def preprocess_worflow() :
    # @task() # task group
    # def check_data_is_updated() :

    #     lag_list = [7, 14, 21] # 1 2 3 semanas por exemplo

    #     # check Utente.csv,  Especialidade, Unidade Saude, Unidade Saude Destino, proveniencia, Geografia are updated
    #     # update csv files

    #     statement1 = 'SELECT * FROM ConsultaMarcacao where DAYS(DATA_CONSULTA - %s) in (%s);' \
    #         % (datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0), lag_list)
    #     consultas_futuras = run_db_statement(statement2)
    #     # write file to csv
    #     nums_sequenciais = consultas_futuras.cenas() # implement funcion

    #     statement2 = 'SELECT * FROM Consulta where NUM_SEUQNCIAL in (%s) AND DAYS(%s - DATA_CONSULTA) <= 30;' % (today, nums_sequenciais)
    #     consultas = run_db_statement(statement2)
    #     # write file to csv

    #     statement3 = 'SELECT * FROM Marcacao where NUM_SEUQNCIAL in (%s)AND DAYS(%s - DATA_CONSULTA) <= 30;' % (today, nums_sequenciais)
    #     consultas_marcacao = run_db_statement(statement3)
    #     # update consulta_marcacao.csv

    #     return True

    #@task()
    def inference(test_ds) :
        return test_ds


    #@task()
    def load_preds_to_db(preds) :
        print(preds)


    # is_updated = check_data_is_updated()
    def task_run_notebook(filepath: str) :
        assert os.path.exists(filepath)
        location, name = os.path.split(filepath)

        pm.execute_notebook(
            filepath,
            os.path.join(location, f"out_{name}"),
            kernel_name='python3'
        )

    # @task()
    t1 = PythonSensor(
        task_id="run_1_train_test_split_ipynb", 
        python_callable=task_run_notebook(filepath="/opt/airflow/dags/notebooks/1_train_test_split.ipynb")
    )

    # t2 = PythonSensor(
    #     task_id="run_geo_ipynb", 
    #     python_callable=task_run_notebook(filepath="/opt/airflow/dags/notebooks/geo.ipynb")
    # )

    t3 = PythonSensor(
        task_id="run_utente_ipynb", 
        python_callable=task_run_notebook(filepath="/opt/airflow/dags/notebooks/utente.ipynb")
    )

    t4 = PythonSensor(
        task_id="run_2_cl_dataset_ipynb", 
        python_callable=task_run_notebook(filepath="/opt/airflow/dags/notebooks/2_cl_dataset.ipynb")
    )
    
    t5 = PythonSensor(
        task_id="inference_task", 
        python_callable=inference("yay")
    )

    t6 = PythonSensor(
        task_id="save_task", 
        python_callable=load_preds_to_db("yay")
    )

    [t3, t4] << t5 << t6
    #t2 >> t3
    t1 >> t4

preprocess_worflow()