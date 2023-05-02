import sqlalchemy

# TODO: check apache-airflow-providers-common-sql and the examples
def sql_to_pandas(statement: str, db_url: str) :
    engine = sqlalchemy.create_engine(db_url)
    print("Yay")
    with engine.connect() as conn :
        print(conn.execute(sqlalchemy.text(statement)))


# statement = "SELECT TOP (10) [Id] FROM [dbo].[Table1];"
# statement = "SELECT TOP (10) [Id] FROM [MyDb].[dbo].[Table1];"
statement = "SELECT TOP (10) * FROM [dbo].[Table1];"
# statement = "SELECT TOP (10) [Id] FROM [dbo].[Table1];"
# statement = "SELECT TOP (10) [Id] FROM [dbo].[Table1];"

host = "host.docker.internal"

db_url=f"mssql+pyodbc://TestUser:123@{host}:1433/MyDb"


# Microsoft ODBC Driver 18 for SQL Server
driver = "ODBC Driver 17 for SQL Server"
if driver != "" : db_url = f"{db_url}?driver={driver.replace(' ', '+')}"

# ?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server

# db_url="mssql+pyodbc://TestUser:123@localhost:1433/MyDb?driver=SQL+Server"
sql_to_pandas(statement, db_url)