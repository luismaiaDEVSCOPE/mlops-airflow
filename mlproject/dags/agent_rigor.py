import sys, os
import datetime
from airflow.models import DAG
from airflow.operators.python import PythonVirtualenvOperator, PythonOperator 
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator

# Add root source to PATH
MLPROJECT = '/opt/airflow'  
# MLPROJECT = 'C:\DVS_Git\mlops-airflow\mlproject'
sys.path.append(MLPROJECT)
from engine.helpers import connections

from datetime import date, timedelta
today = date.today()
today_day = today.day - 1 if today.day > 1 else today.day

default_args = {
    'depends_on_past': False,
    'email': ['youemail@mail.net'],
    'email_on_failure': False,
    'email_on_retry': False,
    'owner': 'DevScope',
    'start_date': datetime.datetime(today.year, month=today.month, day=today_day),
    'retries': 3,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG(
    'workshop_workflow',
    schedule=timedelta(days=1),  # Changed from schedule_interval to schedule
    default_args=default_args,
    catchup=False,
    tags=['workshop', 'ml-pipeline']  # Added tags for better organization
)

def read_requirements_from_client(client:str):
    requirements = list()
    try:
        with open(f'/opt/airflow/dags/clients/{client}/requirements.txt', 'r') as f :
            for line in f:
                print(line)
                requirements.append(line.rstrip())
    except Exception as ex:
        print(ex)
        raise
    return requirements

def run_from_client(client:str, notebook:str):
    print('running code')

    pass

def extract_data_function():
    from engine.scripts.extracts import sql_extract
    
    task = PythonVirtualenvOperator(
        task_id="run_extract",
        python_callable=sql_extract.run,
        requirements=read_requirements_from_client('class1'),
        system_site_packages=False,
        op_kwargs={'dataset': 'dataset_name','conn_type': 'mssql'},
    )
    return task

def transform_data_function():
    #TODO: Execute your data cleaning
    return 

def load_data_function():
    #TODO: Generate your data to be used
    return 

def predict_function():
    from engine.scripts.predict import exec_notebook
    # from airflow.providers.papermill.operators.papermill import PapermillOperator
    # run_this = PapermillOperator(
    #     task_id="run_example_notebook",
    #     input_nb="/tmp/hello_world.ipynb",
    #     output_nb="/tmp/out-{{ execution_date }}.ipynb",
    #     parameters={"msgs": "Ran from Airflow at {{ execution_date }}!"},
    # )
    task = PythonVirtualenvOperator(
        task_id="run_predict",
        python_callable=exec_notebook.run,
        requirements=['jupyter','ipykernel', 'pandas','scikit-learn','matplotlib','papermill'],
        system_site_packages=False,
        dag=dag,
        op_kwargs={'notebook': '/opt/airflow/dags/clients/class1/iris.ipynb',
                    'out_notebook': '/opt/airflow/dags/clients/class1/out_iris.ipynb'},
    )
    return task

def this_will_fail():
    task = BashOperator(
        task_id='notebook_run',
        bash_command='jupyter nbconvert --to notebook --execute /opt/airflow/dags/clients/class1/iris.ipynb',
        dag=dag,
    )
    return task

start_node = EmptyOperator(task_id='etl_start',dag=dag)
end_node = EmptyOperator(task_id='etl_finish', dag=dag)

def create_graph():
    start_node >> extract_data_function() >> [this_will_fail(), predict_function()] >> end_node

create_graph()