import pandas as pd

df = pd.read_csv("policefinal.csv")

for index in range(len(df)):
	if df.loc[index, 'Category'] in ['DRIVING UNDER THE INFLUENCE', 'NON-CRIMINAL','DRUNKENNESS','TRESPASS', 'DISORDERLY CONDUCT','GAMBLING', 'LOITERING', 'LIQUOR LAWS']:
		df.loc[index, 'CrimeClass'] = 'PUBLIC MISCONDUCT'

	if df.loc[index, 'Category'] in ['EXTORTION']:
		df.loc[index, 'CrimeClass'] = 'CORRUPTION'

	if df.loc[index, 'Category'] in ['ASSAULT', 'WEAPON LAWS']:
		df.loc[index, 'CrimeClass'] = 'ASSAULT'

	if df.loc[index, 'Category'] in ['RUNAWAY','KIDNAPPING','MISSING PERSON']:
		df.loc[index, 'CrimeClass'] = 'MISSING PERSON'

	if df.loc[index, 'Category'] in ['ARSON', 'STOLEN PROPERTY', 'VANDALISM']:
		df.loc[index, 'CrimeClass'] = 'PROPERTY DAMAGE'

df.to_csv (r'C:\Users\ACER\Downloads\bytecamp\criminal offense\reclassified.csv', index = None, header=True)