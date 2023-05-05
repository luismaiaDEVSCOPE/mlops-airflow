import pandas as pd
import sqlalchemy


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

def pandas_to_sql(statement: str, df: pd.DataFrame, db_url: str) :
    engine = sqlalchemy.create_engine(db_url)

    with engine.connect() as conn :
        for row in df.itertuples(index=False, name=None) :
            conn.execute(statement % (str(row)))


if __name__ == "__main__" :
    df = pd.DataFrame({
    "Id": [4, 5, 6],
    "Text": ["Text40", "Text50", "Text60"]})

    db_url = get_db_url(
        connection_name="test_con", 
        dialect="mssql+pyodbc", 
        driver="ODBC+Driver+17+for+SQL+Server")
    
    statement = "INSERT INTO [dbo].[Table1] (Id, Text) VALUES %s;"
    pandas_to_sql(statement, df, db_url)
