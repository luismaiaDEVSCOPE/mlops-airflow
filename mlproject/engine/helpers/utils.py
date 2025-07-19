import os 
import pandas as pd
from airflow.providers.papermill.operators.papermill import PapermillOperator

def requirments_as_list(requirements_path: str) :
    requirements = []
    assert os.path.exists(requirements_path) 

    try:
        with open(requirements_path, 'r') as f :
            for line in f.readlines() :
                line = line.strip()

                if not line.startswith("#") :
                    print(line)
                    requirements.append(line)

    except Exception as ex:
        print(ex)
        raise

    return requirements


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


# TODO: check apache-airflow-providers-common-sql and the examples
def sql_to_pandas(statement: str, engine) -> pd.DataFrame :
    with engine.connect() as conn :

        # TODO: Check if the statement is valid
        # statement = statement.compile(engine)
        result = conn.execute(statement)
        
        # df = pd.DataFrame(result.fetchall())
        # df.columns = result.keys()

        # TODO: Check for memory limitations
        result_frame = pd.DataFrame =\
            pd.DataFrame(result.fetchall(), columns=result.keys()) # Yield instead of return
        
    return result_frame


def get_db_engine(connection_name: str, dialect=None, driver=None) :
    from airflow.hooks.base import BaseHook
    import sqlalchemy
    conn = BaseHook.get_connection(connection_name)
    # testing connection = host.docker.internal:1433
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

    return sqlalchemy.create_engine(base_string % tuple(values_list))
