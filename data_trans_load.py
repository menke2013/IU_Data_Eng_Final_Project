<<<<<<< HEAD
import sys
import numpy as np
import pandas as pd
import logging
from cassandra.cluster import Cluster


    
cluster = Cluster(['127.0.0.1'], port=9042)
session = cluster.connect()
    
file_name = sys.argv[1]

df_data1 = pd.read_csv(file_name)
df_data1.replace(['00:0f:00:70:91:0a', '1c:bf:ce:15:ec:4d', 'b8:27:eb:bf:9d:51'], ['sensor1', 'sensor2', 'sensor3'], inplace=True)
df_data1['time_stamp'] = pd.to_datetime(df_data1['ts'],unit='s')
df_data1 =df_data1.rename(columns={'device' :'sensor'})
df_data1.drop(columns=['ts'], inplace=True)

query_insert = "INSERT INTO sensorbase.table1 (sensor, co, humidity, light, lpg, motion, smoke, temp, time_stamp) " \
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"

prepared = session.prepare(query_insert)

for index, row in df_data1.iterrows():
    session.execute(prepared
                    , (row['sensor']
                    , row['co']
                    , row['humidity']
                    , row['light']
                    , row['lpg']
                    , row['motion']
                    , row['smoke']
                    , row['temp']
                    , row['time_stamp']))
    


=======
import sys
import numpy as np
import pandas as pd
import logging
from cassandra.cluster import Cluster


    
cluster = Cluster(['127.0.0.1'], port=9042)
session = cluster.connect()
    
file_name = sys.argv[1]

df_data1 = pd.read_csv(file_name)
df_data1.replace(['00:0f:00:70:91:0a', '1c:bf:ce:15:ec:4d', 'b8:27:eb:bf:9d:51'], ['sensor1', 'sensor2', 'sensor3'], inplace=True)
df_data1['time_stamp'] = pd.to_datetime(df_data1['ts'],unit='s')
df_data1 =df_data1.rename(columns={'device' :'sensor'})
df_data1.drop(columns=['ts'], inplace=True)

query_insert = "INSERT INTO sensorbase.table1 (sensor, co, humidity, light, lpg, motion, smoke, temp, time_stamp) " \
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"

prepared = session.prepare(query_insert)

for index, row in df_data1.iterrows():
    session.execute(prepared
                    , (row['sensor']
                    , row['co']
                    , row['humidity']
                    , row['light']
                    , row['lpg']
                    , row['motion']
                    , row['smoke']
                    , row['temp']
                    , row['time_stamp']))
    


>>>>>>> 4f7da5abe1d5cc6a587e101dc6327b7795e2ed4f
