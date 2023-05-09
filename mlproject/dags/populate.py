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


def insert_from_pandas(db_url, df, table_name) :
    columns_str = str(df.columns.tolist())\
                    .replace("', '", "], [")\
                    .replace("'", "")
    columns_str = "("+columns_str+")"

    statement = f"INSERT INTO {table_name} {columns_str} VALUES "
    statement+=" %s ;"

    pandas_to_sql(statement, df, db_url)


if __name__ == "__main__" :

    db_url = get_db_url(
        connection_name="test_con", 
        dialect="mssql+pyodbc", 
        driver="ODBC+Driver+17+for+SQL+Server")
    
    engine = sqlalchemy.create_engine(db_url)


    # df = pd.DataFrame({ "Id": [4, 5, 6], "Text": ["Text40", "Text50", "Text60"]})
    # columns = " (Id, Text)"
    # table_name = "[dbo].[Table1]"
    

    consulta = pd.read_csv('/opt/airflow/datasets/absenteeism/Consulta.txt', 
                            sep='|', 
                            encoding="ISO-8859-1")\
        .convert_dtypes()
    consulta.to_sql("Consulta", engine, if_exists="append", index=False)
    print("Con Done")

    pd.read_csv('/opt/airflow/datasets/absenteeism/Utentes.txt', sep='|', encoding="ISO-8859-1").convert_dtypes()\
        .to_sql("Utente", engine, if_exists="append", index=False)
    print("Ut Done")

    pd.read_csv('/opt/airflow/datasets/absenteeism/ConsultaMarcacao.txt', sep='|', encoding="ISO-8859-1").convert_dtypes()\
        .to_sql("Consulta Marcação", engine, if_exists="append", index=False)
    print("ConMarc Done")

    pd.read_csv('/opt/airflow/datasets/absenteeism/Geografia.txt', sep='|', encoding="ISO-8859-1").convert_dtypes()\
        .to_sql("Geografia", engine, if_exists="append", index=False)
    print("Geografia Done")

    pd.read_csv('/opt/airflow/datasets/absenteeism/Especialidade.txt', sep=',', encoding="ISO-8859-1").convert_dtypes()\
        .to_sql("Especialidade", engine,  if_exists="append", index=False)
    print("Esp Done")


    pd.read_csv('/opt/airflow/datasets/absenteeism/unisau.txt', sep='|', encoding="ISO-8859-1").convert_dtypes()\
      .to_sql("Unidade Saúde Proveniência", engine, if_exists="append", index=False)
    print("Uni Sau prov Done")