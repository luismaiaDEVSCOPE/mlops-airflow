
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

    @task
    def get_data_from_consulta_marcacao_table(conn_str) :
        pass

    @task
    def get_data_from_consulta_table(conn_str) :
        pass

    @task
    def get_data_from_utente_table(conn_str) :
        pass

    @task()
    def get_unidade_saude_table(conn_str) :
        pass

    @task()
    def get_porveniencia_table(conn_str) :
        pass

    @task()
    def get_especialidade_table(conn_str) :
        pass

    @task()
    def get_unidade_destino_table(conn_str) :
        pass

    @task()
    def get_geography_table(conn_str) :
        pass

    @task()
    def generate_coordenates() :
        from geo import geo_script
        geo_script()
        return True


    @task()
    def load_preds_to_db(conn_str) :
        # mlflow.sklearn.log_model(clf, RUN_NAME)
        print("loading to database")
        return True


    @task()
    def test_db_conn() :

        def get_db_url(connection_name: str, dialect=None, driver=None) :
            from airflow.hooks.base import BaseHook
            conn = BaseHook.get_connection(connection_name)
            base_string = "%s://%s:%s@%s:%s/%s"

            # values to build the connection string
            # note: sometimes airflow may not have the ideal dialect
            values_list = [conn.conn_type if dialect is None else dialect, conn.login, 
                           conn.password, conn.host, conn.port, conn.schema]

            # A specific driver may be required. If so add both the value and text to the connection string
            if not driver is None :
                base_string += "?driver=%s"
                values_list.append(
                    driver if " " in driver else driver.replace(' ', '+'))

            return base_string % tuple(values_list)


        db_url = get_db_url(
            connection_name="test_con", 
            dialect="mssql+pyodbc", 
            driver="ODBC+Driver+17+for+SQL+Server")

        import sqlalchemy
        import pandas as pd

        engine = sqlalchemy.create_engine(db_url)
        statement = "SELECT TOP (10) * FROM [dbo].[Table1];"

        with engine.connect() as conn :
            result = conn.execute(statement)
            yield pd.DataFrame(result.fetchall(), columns=result.keys())
  

    # is_updated = check_data_is_updated()
    def task_run_notebook(filepath: str) :
        # import papermill as pm
        assert os.path.exists(filepath)
        location, name = os.path.split(filepath)

        return PapermillOperator(
            task_id=f"run_{name}",
            input_nb=filepath, 
            output_nb=os.path.join(location, "out_folder", name),
            # parameters={"msgs": "Ran from Airflow at {{ execution_date }}!"},
        )

    # t1 = task_run_notebook(filepath="/opt/airflow/dags/notebooks/data_split.ipynb")
    # t2 = task_run_notebook(filepath="/opt/airflow/dags/notebooks/geo.ipynb")
    t2 = PythonSensor(
        task_id="geo_task", 
        python_callable=generate_coordenates
    )

    t3 = task_run_notebook(filepath="/opt/airflow/dags/notebooks/utente.ipynb")

    t4 = task_run_notebook(filepath="/opt/airflow/dags/notebooks/main_data_prep.ipynb")

    t5 = task_run_notebook(filepath="/opt/airflow/dags/notebooks/inference_4_prod.ipynb")


    # t6 = PythonSensor(
    #     task_id="save_task", 
    #     python_callable=load_preds_to_db
    # )

    # testing connection = host.docker.internal:1434 ou host.docker.internal:1433


    # EmptyOperator(task_id="first") >> db_check() >> [t1, t2] 
    #EmptyOperator(task_id="first") >> test_db_conn() 

    """
    test_db_conn() >> [# [get_data_from_consulta_table(), get_data_from_utente_table()] <<  get_data_from_consulta_marcacao_table(),
                  get_geography_table() >> t2, 
                  get_especialidade_table(),
                  get_porveniencia_table(),
                  get_unidade_destino_table(),
                  get_unidade_saude_table()] >> t4
    """

    conn_str = test_db_conn()

    f1 = get_data_from_consulta_table(conn_str)
    f2 = get_data_from_utente_table(conn_str)
    f3 = get_data_from_consulta_marcacao_table(conn_str)

    f4 = get_geography_table(conn_str)
    f5 = get_especialidade_table(conn_str)
    f6 = get_porveniencia_table(conn_str)
    f7 = get_unidade_destino_table(conn_str)
    f8 = get_unidade_saude_table(conn_str)

    f9 = load_preds_to_db(conn_str)

    f4 >> t2 >> t3

    # t2 >> t3
    [f1, f2, f3, f5, f6, f7, f8] >> t4
    [t3, t4] >> t5 >> f9 # >> EmptyOperator(task_id="last")

   
main_worflow()