import sqlalchemy

# TODO: check apache-airflow-providers-common-sql and the examples
def sql_to_pandas(statement: str, db_url: str) :
    engine = sqlalchemy.create_engine(db_url)
    print("Yay")
    with engine.connect() as conn :
        print(conn.execute(sqlalchemy.text(statement)))


def test_func() :
    # statement = "SELECT TOP (10) [Id] FROM [dbo].[Table1];"
    # statement = "SELECT TOP (10) [Id] FROM [MyDb].[dbo].[Table1];"
    statement = "SELECT TOP (10) * FROM [dbo].[Table1];"
    # statement = "SELECT TOP (10) [Id] FROM [dbo].[Table1];"
    # statement = "SELECT TOP (10) [Id] FROM [dbo].[Table1];"

    # Microsoft ODBC Driver 18 for SQL Server
    driver = "ODBC Driver 17 for SQL Server"
    if driver != "" : db_url = f"{db_url}?driver={driver.replace(' ', '+')}"

    # ?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server
    # db_url="mssql+pyodbc://TestUser:123@localhost:1433/MyDb?driver=SQL+Server"
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


if __name__ == "__main__" :
    db_check()
