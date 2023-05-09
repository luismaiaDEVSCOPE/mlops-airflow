import sqlalchemy
import pandas as pd
import os

def test_func() :
    statement = "SELECT TOP (10) * FROM [dbo].[Table1];"

    # Microsoft ODBC Driver 18 for SQL Server
    driver = "ODBC Driver 17 for SQL Server"
    if driver != "" : db_url = f"{db_url}?driver={driver.replace(' ', '+')}"

    # ?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server
    # db_url="mssql+pyodbc://<user>:<password>@<host>:<port>/<db-name>?driver=SQL+Server"
    sql_to_pandas(statement, db_url)


def get_db_url(connection_name: str, dialect=None, driver=None) :
    from airflow.hooks.base import BaseHook
    conn = BaseHook.get_connection(connection_name)
    base_string = "%s://%s:%s@%s:%s/%s"

    values_list = [conn.conn_type if dialect is None else dialect, conn.login, conn.password, 
                   conn.host, conn.port, conn.schema]

    if not driver is None :
        base_string += "?driver=%s"
        values_list.append(
            driver if " " in driver else driver.replace(' ', '+'))

    return base_string % tuple(values_list)


def db_check() :
    db_url = get_db_url(
        connection_name="test_con", 
        dialect="mssql+pyodbc", 
        driver="ODBC+Driver+17+for+SQL+Server")

    import sqlalchemy

    engine = sqlalchemy.create_engine(db_url)
    statement = "SELECT TOP (10) * FROM [dbo].[Table1];"

    with engine.connect() as conn :
        print(conn.execute(sqlalchemy.text(statement)))


def sql_to_pandas(statement: str, db_url: str) -> pd.DataFrame :
    engine = sqlalchemy.create_engine(db_url)

    with engine.connect() as conn :
        result = conn.execute(statement)

        result_frame = pd.DataFrame =\
            pd.DataFrame(result.fetchall(), columns=result.keys()) # Yield instead of return
        
    return result_frame


if __name__ == "__main__" :
    db_url = get_db_url(
        connection_name="test_con", 
        dialect="mssql+pyodbc", 
        driver="ODBC+Driver+17+for+SQL+Server")
    
    script_path = os.path.abspath(os.path.dirname(__file__))

    path = os.path.join(script_path, 
        "statements/consulta_marcacao.sql")

    statement = ""
    with open(path, "r") as f :
        statement = f.read()

    path = os.path.join(script_path, 
        "statements/esp_keys.json")
    
    esp_key_str = ""
    with  open(path, "r") as f :
        esp_key_str = f.read()

    esp_key_str = esp_key_str.replace('[', '').replace(']', '')
    statement = statement % ("day", "01/24/2023", 7, esp_key_str)
    # print(statement)

    df : pd.DataFrame = sql_to_pandas(statement, db_url)
    print(df)