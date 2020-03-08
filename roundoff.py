import pandas as pd
import numpy as np

df = pd.read_csv("policefinal.csv")

# for i in range(len(df)):
#     mydate =  df.loc[i, 'Time']
#     mydate = mydate.split(':')
#     mins = int(mydate[1])
#     hrs = int(mydate[0])
#     if mins >= 0 and mins <= 15:
#         df.loc[i, 'roundedtime'] = str(hrs) + ':00'
#     elif mins > 15 and mins <45:
#         df.loc[i, 'roundedtime'] = str(hrs) + ':30'
#     elif mins >= 45:
#         if hrs == 23:
#             df.loc[i, 'roundedtime'] = '00:00'
#         else:
#             df.loc[i, 'roundedtime'] = str(hrs+1) + ':00' 


df = df.insert(loc=0, column='SrNo', value=np.arange(len(df)))


df.to_csv (r'C:\Users\ACER\Downloads\bytecamp\criminal offense\roundedtime.csv', index = None, header=True)