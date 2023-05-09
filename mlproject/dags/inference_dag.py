
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
from airflow.decorators import dag , task
from airflow.sensors.python import PythonSensor
from airflow.operators.empty import EmptyOperator

# from sqlalchemy import create_engine
# from sqlalchemy.engine import URL
# import pandas as pd

# # Using db from https://rnacentral.org/help/public-database
# url_object = URL.create('postgresql+psycopg2', 
#     username='reader', password='NWDMCE5xdipIjRrp', 
#     host='hh-pgsql-public.ebi.ac.uk', port='5432', 
#     database='pfmegrnargs')

# def run_db_statement(statement) :
#     with create_engine(url_object).connect() as conn :
#         res = conn.execute(statement)
#         yield pd.DataFrame(res.fetchall(), columns=res.keys())

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

@dag(schedule_interval="0 0 1 * * *", #"@daily",
    start_date=datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0),
    catchup=False,
    tags=["inference"],
    default_args=args
    )

def main_worflow() :
    import utils
    SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

    @task
    def get_data_from_consulta_marcacao_table(engine) :
        import utils

        path = os.path.join(SCRIPT_PATH, 
            "statements/consulta_marcacao.sql")

        statement = ""
        with open(path, "r") as f :
            statement = f.read()

        path = os.path.join(SCRIPT_PATH, 
            "statements/esp_keys.sql")
        
        esp_query_str = ""
        with  open(path, "r") as f :
            esp_query_str = f.read()

        statement = statement % ("day", "01/24/2023", 7, esp_query_str)
        # print(statement)

        return utils.sql_to_pandas(statement, engine)


    @task
    def get_data_from_consulta_table(engine, con_marc) :
        path = os.path.join(SCRIPT_PATH, 
            "statements/consulta.sql")

        statement = ""
        with open(path, "r") as f :
            statement = f.read()

        path = os.path.join(SCRIPT_PATH, 
            "statements/esp_keys.sql")
        
        esp_query_str = ""
        with  open(path, "r") as f :
            esp_query_str = f.read()

        nums = str( set( con_marc['Nº Sequencial'].copy().astype(int) ) )\
            .replace('{', '').replace('}', '')
        # print(nums)

        statement = statement % ("day", "01/24/2023", 30, nums, esp_query_str)
        # print(statement)

        return utils.sql_to_pandas(statement, engine)


    @task
    def get_data_from_utente_table(engine, con_marc) :
        path = os.path.join(SCRIPT_PATH, 
            "statements/utente.sql")

        statement = ""
        with open(path, "r") as f :
            statement = f.read()

        nums = str( set( con_marc['Nº Sequencial'].copy().astype(int) ) )\
            .replace('{', '').replace('}', '')
        # print(nums)

        statement = statement % (nums)
        # print(statement)

        return utils.sql_to_pandas(statement, engine)
    

    @task()
    def get_unidade_saude_table(engine) :
        pass

    @task()
    def get_porveniencia_table(engine) :
        pass

    @task()
    def get_especialidade_table(engine) :
        pass

    @task()
    def get_unidade_destino_table(engine) :
        pass

    @task()
    def get_geography_table(engine) :
        pass


    @task()
    def get_coords() :
        from geo import geo_script
        return geo_script()


    @task()
    def load_preds_to_db(engine) :
        print("loading to database")
        return True


    @task()
    def get_db_engine(connection_name, dialect, driver) :
        return utils.get_db_engine(
            connection_name=connection_name, 
            dialect=dialect, 
            driver=driver)


    # t1 = task_run_notebook(filepath="/opt/airflow/dags/notebooks/data_split.ipynb")
    # t2 = task_run_notebook(filepath="/opt/airflow/dags/notebooks/geo.ipynb")

    t3 = utils.task_run_notebook(filepath="/opt/airflow/dags/notebooks/utente.ipynb")

    t4 = utils.task_run_notebook(filepath="/opt/airflow/dags/notebooks/main_data_prep.ipynb")

    t5 = utils.task_run_notebook(filepath="/opt/airflow/dags/notebooks/inference_4_prod.ipynb")

    # t6 = PythonSensor(
    #     task_id="save_task", 
    #     python_callable=load_preds_to_db
    # )

    # EmptyOperator(task_id="first")
    # EmptyOperator(task_id="first") 

    engine = get_db_engine(connection_name="test_con", 
            dialect="mssql+pyodbc", 
            driver="ODBC+Driver+17+for+SQL+Server")

    consulta_marcacao = get_data_from_consulta_marcacao_table(engine)
    consulta = get_data_from_consulta_table(engine, consulta_marcacao)
    utente = get_data_from_utente_table(engine, consulta_marcacao)
    

    f4 = get_geography_table(engine)
    f5 = get_especialidade_table(engine)
    f6 = get_porveniencia_table(engine)
    f7 = get_unidade_destino_table(engine)
    f8 = get_unidade_saude_table(engine)

    f9 = load_preds_to_db(engine)

    # get_coords() - geo - precisa de GEO
    # t3 - utentes - precisa de UTENTES e do geo_cords (resultado de geo_script)
    # t4 - main_data_prep - precisa CONSULTA CONSULTA_MARC (UNISAU e ESP)
    # t5 - infrecence prod - precisa utentes e consultas (resultado t4 e resultado t3)

    f4 >> t2 >> t3
    f2 >> t3

    [f1, f2, f3, f5, f6, f7, f8] >> t4
    [t3, t4] >> t5 >> f9


main_worflow()