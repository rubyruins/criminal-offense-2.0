# a script to segregate various crimes into nine main classes

import pandas as pd

df = pd.read_csv("policenew.csv")

for index in range(len(df)):
	if df.loc[index, 'Category'] in ['BURGLARY', 'ROBBERY', 'LARCENY/THEFT', 'VEHICLE THEFT', 'RECOVERED VEHICLE']:
		df.loc[index, 'CrimeClass'] = 'THEFT'
	if df.loc[index, 'Category'] in ['DRIVING UNDER THE INFLUENCE', 'NON-CRIMINAL','DRUNKENNESS','TRESPASS', 'DISORDERLY CONDUCT','GAMBLING', 'LOITERING', 'LIQUOR LAWS']:
		df.loc[index, 'CrimeClass'] = 'NON CRIMINAL'
	if df.loc[index, 'Category'] in ['BRIBERY','FORGERY/COUNTERFEITING','FRAUD', 'EMBEZZLEMENT', 'EXTORTION']:
		df.loc[index, 'CrimeClass'] = 'CORRUPTION'
	if df.loc[index, 'Category'] in ['SUICIDE']:
		df.loc[index, 'CrimeClass'] = 'LOSS OF LIFE'
	if df.loc[index, 'Category'] in ['SEX OFFENSES, NON FORCIBLE', 'SEX OFFENSES, FORCIBLE','PORNOGRAPHY/OBSCENE MAT','PROSTITUTION',
	'DRUG/NARCOTIC']:
		df.loc[index, 'CrimeClass'] = 'SEX OFFENSES'
	if df.loc[index, 'Category'] in ['OTHER OFFENSES', 'WARRANTS' ,'SECONDARY CODES', 'SUSPICIOUS OCC', 'FAMILY OFFENSES', 'TREA','BAD CHECKS']:
		df.loc[index, 'CrimeClass'] = 'OTHER CRIMES'
	if df.loc[index, 'Category'] in ['ASSAULT', 'WEAPON LAWS']:
		df.loc[index, 'CrimeClass'] = 'ASSAULT'
	if df.loc[index, 'Category'] in ['RUNAWAY','KIDNAPPING','MISSING PERSON']:
		df.loc[index, 'CrimeClass'] = 'MISSINGPERSON'
	if df.loc[index, 'Category'] in ['ARSON',, 'STOLEN PROPERTY', 'VANDALISM']:
		df.loc[index, 'CrimeClass'] = 'PROPERTYDAMAGE'
	


df.to_csv (r'C:\Users\parekh\Downloads\bytecamp\finalpolice.csv', index = None, header=True)
