import os 
import pandas as pd
import sqlalchemy

import airflow.providers.papermill.operators.papermill as afl_pml
# from airflow.providers.papermill.operators.papermill import PapermillOperator

def task_run_notebook(filepath: str) :
    assert os.path.exists(filepath)

    location, name = os.path.split(filepath)

    return afl_pml.PapermillOperator(
        task_id=f"run_{name}",
        input_nb=filepath, 
        output_nb=os.path.join(location, f"out_{name}"),
        # parameters={"msgs": "Ran from Airflow at {{ execution_date }}!"},
    )   


def requirments_as_list(requirements_path: str) :
    requirements = []
    assert os.path.exists(requirements_path) 

    try:
        with open(requirements_path, 'r') as f :
            for line in f.readlines():
                print(line)
                requirements.append(line.rstrip())

    except Exception as ex:
        print(ex)
        raise

    return requirements

# TODO: check apache-airflow-providers-common-sql and the examples
def sql_to_pandas(statement: str, db_url: str) :
    engine = sqlalchemy.create_engine(db_url)
    with engine.connect() as conn :

        # TODO: Check if the statement is valid
        # statement = statement.compile(engine)
        result = conn.execute(statement)
        
        # df = pd.DataFrame(result.fetchall())
        # df.columns = result.keys()

        # TODO: Check for memory limitations
        yield pd.DataFrame(result.fetchall(), columns=result.keys()) # Yield instead of return