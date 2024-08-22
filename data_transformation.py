import sys
import numpy as np
import pandas as pd

file_name = sys.argv[1]

df_data1 = pd.read_csv(file_name)
df_data1.replace(['00:0f:00:70:91:0a', '1c:bf:ce:15:ec:4d', 'b8:27:eb:bf:9d:51'], ['sensor1', 'sensor2', 'sensor3'], inplace=True)
df_data1['time_stamp'] = pd.to_datetime(df_data1['ts'],unit='s')
df_data1 =df_data1.rename(columns={'device' :'sensor'})
df_data1.drop(columns=['ts'], inplace=True)


df_data1.to_csv('data_updated.csv', sep=',', encoding='utf-8', index=False, header=False)

