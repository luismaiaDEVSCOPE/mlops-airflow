def run(**kwargs):
    print('####################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$##############################')
    import sys
    import csv as csv
    from sqlalchemy import create_engine, exc
    # Add root source to PATH
    MLPROJECT = '/opt/airflow' 
    # MLPROJECT = 'C:\DVS_Git\mlops-airflow\mlproject'
    sys.path.append(MLPROJECT)
    from engine.helpers import connections
    import engine.config as config

    # if __debug__:
    #     kwargs.update(dataset='irisdataset')
    #     kwargs.update(conn_type='mssql')
    dataset = kwargs['dataset']
    conn_type = kwargs['conn_type']
    source = 'db_source' #config.db_config_source
    db_url = connections.get_airflow_connection(source)
    print(db_url)
    engine = create_engine(db_url)
    with engine.connect() as conn:
        result = conn.execute('''SELECT * \
                                FROM [dbo].[iris_data]''')
        with open(f'{MLPROJECT}/datasets/{dataset}.csv', "w+", newline='', encoding='utf-8') as f:
            csv_writer = csv.writer(f, delimiter=',',quotechar="'", quoting=csv.QUOTE_NONNUMERIC)
            csv_writer.writerow([r for r in result._metadata.keys])
            x = 0
            for row in result:
                csv_writer.writerow([column for column in row])
                x += 1
            print("Finished writing file: {x} rows in '{file}'".format(x=x, file=f.name))

# if __debug__:
#     run()