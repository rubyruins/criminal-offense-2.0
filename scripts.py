# a script to segregate various crimes into six main classes

import pandas as pd

df = pd.read_csv("policefinal.csv")

for i in range(len(df)):
    df.loc[i, 'IncidntNum'] = str(df.loc[i, 'IncidntNum'])
    df.loc[i, 'PdId'] = str(df.loc[i, 'PdId'])

print(df.info())

# df['IncidntNum'] = df['IncidntNum'].astype(str)
# df['PdId'] = df['PdId'].astype(str)

# initial segregation

# for index in range(len(df)):
# 	if df.loc[index, 'Category'] in ['BURGLARY', 'ROBBERY', 'LARCENY/THEFT', 'STOLEN PROPERTY', 'VEHICLE THEFT', 'RECOVERED VEHICLE']:
# 		df.loc[index, 'CrimeClass'] = 'THEFT'
# 	if df.loc[index, 'Category'] in ['DRIVING UNDER THE INFLUENCE', 'NON-CRIMINAL', 'VANDALISM','ARSON','DRUNKENNESS','TRESPASS','RUNAWAY', 'DISORDERLY CONDUCT','GAMBLING']:
# 		df.loc[index, 'CrimeClass'] = 'NON CRIMINAL'
# 	if df.loc[index, 'Category'] in ['BRIBERY','FORGERY/COUNTERFEITING','FRAUD', 'EMBEZZLEMENT']:
# 		df.loc[index, 'CrimeClass'] = 'CORRUPTION'
# 	if df.loc[index, 'Category'] in ['SUICIDE']:
# 		df.loc[index, 'CrimeClass'] = 'LOSS OF LIFE'
# 	if df.loc[index, 'Category'] in ['SEX OFFENSES, NON FORCIBLE', 'SEX OFFENSES, FORCIBLE','PORNOGRAPHY/OBSCENE MAT','PROSTITUTION',
# 	'DRUG/NARCOTIC']:
# 		df.loc[index, 'CrimeClass'] = 'SEX OFFENSES'
# 	if df.loc[index, 'Category'] in ['OTHER OFFENSES','KIDNAPPING', 'WEAPON LAWS', 'WARRANTS',  'ASSAULT','MISSING PERSON', 'SECONDARY CODES', 'SUSPICIOUS OCC', 'FAMILY OFFENSES', 'LIQUOR LAWS', 'EXTORTION', 'LOITERING', 'TREA','BAD CHECKS']:
# 		df.loc[index, 'CrimeClass'] = 'OTHER CRIMES'


# further segregation

# for index in range(len(df)):
# 	if df.loc[index, 'Category'] in ['DRIVING UNDER THE INFLUENCE', 'NON-CRIMINAL','DRUNKENNESS','TRESPASS', 'DISORDERLY CONDUCT','GAMBLING', 'LOITERING', 'LIQUOR LAWS']:
# 		df.loc[index, 'CrimeClass'] = 'PUBLIC MISCONDUCT'

# 	if df.loc[index, 'Category'] in ['EXTORTION']:
# 		df.loc[index, 'CrimeClass'] = 'CORRUPTION'

# 	if df.loc[index, 'Category'] in ['ASSAULT', 'WEAPON LAWS']:
# 		df.loc[index, 'CrimeClass'] = 'ASSAULT'

# 	if df.loc[index, 'Category'] in ['RUNAWAY','KIDNAPPING','MISSING PERSON']:
# 		df.loc[index, 'CrimeClass'] = 'MISSING PERSON'

# 	if df.loc[index, 'Category'] in ['ARSON', 'STOLEN PROPERTY', 'VANDALISM']:
# 		df.loc[index, 'CrimeClass'] = 'PROPERTY DAMAGE'


# refinement

# for index in range(len(df)):
#     if df.loc[index, 'Category'] in ['DRUG/NARCOTIC']:
#             df.loc[index, 'CrimeClass'] = 'OTHER CRIMES'


# split date

# df = df.drop(['Date'], axis=1)
# df = df.rename({"SingleDate": "Date"})

# df['Month'] = df['Month'].astype(str)

# for index in range(len(df)):
#     mydate = df.loc[index, 'Date']
#     mydate = mydate.split("-")
#     # df.loc[index, 'Month'] = mydate[1]
#     df.loc[index, 'SingleDate'] = mydate[0]


# adjust time

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


# add srno

# df = df.insert(loc=0, column='SrNo', value=np.arange(len(df)))

df.to_csv (r'C:\Users\Acer\Downloads\bytecamp\criminal offense\intvalues.csv', index = None, header=True)