#!/usr/bin/env python

def geo_script() :
    import os

    if not os.path.exists('/opt/airflow/datasets/absenteeism/geografia_coord.parquet') : # this vaidation needs to be different outside test context

        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt
        from datetime import datetime
        import ast

        from geopy.geocoders import Nominatim
        from geopy.distance import geodesic


        def convert_str_to_int(x):
            try:
                return(int(float(x)))
            except:
                return(np.nan)


        def get_coord(x):
            try:
                return(x[1])
            except:
                return(None)


        def distance(row): 
            address1 = (row['utente_lat'], row['utente_lon']) 
            address2 = (row['hospital_lat'], row['hospital_lon']) 
            try:
                return (geodesic(address1, address2).kilometers) 
            except: 
                return np.nan


        geografia = pd.read_csv('/opt/airflow/datasets/absenteeism/Geografia.txt', sep='|', encoding="ISO-8859-1")


        #! pip install geopy
        from geopy.geocoders import Nominatim
        from geopy.distance import geodesic


        ##remover do nome  coisas do tipo usf e assim e deixar só o nome da cidade
        geolocator = Nominatim(user_agent="my-application2")

        def locate(x) :
            try :
                return geolocator.geocode(x)
            except Exception :
                with open("/opt/airflow/datasets/geoooo.txt", "a") as f :
                    f.write(x)
                    
                return ""

        geo_output = geografia['Freguesia Geo'].apply(lambda x : locate(x))


        def get_coord(x):
            try:
                return(x[1])
            except:
                return(None)


        geografia['lat'] = pd.DataFrame({'coord':geo_output.tolist()}).coord.apply(lambda x: x[1][0] if get_coord(x)!=None else None)
        geografia['lon'] = pd.DataFrame({'coord':geo_output.tolist()}).coord.apply(lambda x: x[1][1] if get_coord(x)!=None else None)
        geografia.astype('str').to_parquet('/opt/airflow/datasets/absenteeism/geografia_coord.parquet', compression='gzip')

        # geografia.head()

        exit

    else :
        print("Done")