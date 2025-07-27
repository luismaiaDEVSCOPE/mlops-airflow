def get_airflow_connection(conn_name:str):
    connection = dict()
    # return 'mssql://tests_user:9wy82QQMGnVHDFPc@host.docker.internal/irissql?&driver=ODBC+Driver+17+for+SQL+Server'

    from airflow.hooks.base import BaseHook
    conn = BaseHook.get_connection(conn_name)

    host = conn.host
    db_url = '{conn_type}'.format(conn_type='mssql')
    # 'mssql+pymssql://{user}:{pwd}@{server}/{db}'.format(user=user, pwd=pwd, server=server,db=db)

    driver = None # TODO: get driver from connection
    if driver is not None:
        db_url += '+{driver}'.format(driver=driver)

    if 'port' in connection:
        host += ':{port}'.format(port=conn.port)

    if conn.login is not None and conn.login != '':
        login = conn.login

        if conn.password is not None and conn.password != '':
            login = f'{login}:{conn.password}'

        print(f'connection login {login}')
        db_url += '://{login}@{host}/{schema}?&driver=ODBC+Driver+17+for+SQL+Server'.format(login=login, host=host, schema=conn.schema)

    else:
        db_url += '://{host}/{schema}?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server'.format(host=host, schema=conn.schema)

    return db_url # .get_uri()