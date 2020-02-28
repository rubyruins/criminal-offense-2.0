# a script to segregate various crimes into six main classes

import pandas as pd

df = pd.read_csv("policenew.csv")

for index in range(len(df)):
	if df.loc[index, 'Category'] in ['BURGLARY', 'ROBBERY', 'LARCENY/THEFT', 'STOLEN PROPERTY', 'VEHICLE THEFT', 'RECOVERED VEHICLE']:
		df.loc[index, 'CrimeClass'] = 'THEFT'
	if df.loc[index, 'Category'] in ['DRIVING UNDER THE INFLUENCE', 'NON-CRIMINAL', 'VANDALISM','ARSON','DRUNKENNESS','TRESPASS','RUNAWAY', 'DISORDERLY CONDUCT','GAMBLING']:
		df.loc[index, 'CrimeClass'] = 'NON CRIMINAL'
	if df.loc[index, 'Category'] in ['BRIBERY','FORGERY/COUNTERFEITING','FRAUD', 'EMBEZZLEMENT']:
		df.loc[index, 'CrimeClass'] = 'CORRUPTION'
	if df.loc[index, 'Category'] in ['SUICIDE']:
		df.loc[index, 'CrimeClass'] = 'LOSS OF LIFE'
	if df.loc[index, 'Category'] in ['SEX OFFENSES, NON FORCIBLE', 'SEX OFFENSES, FORCIBLE','PORNOGRAPHY/OBSCENE MAT','PROSTITUTION',
	'DRUG/NARCOTIC']:
		df.loc[index, 'CrimeClass'] = 'SEX OFFENSES'
	if df.loc[index, 'Category'] in ['OTHER OFFENSES','KIDNAPPING', 'WEAPON LAWS', 'WARRANTS',  'ASSAULT','MISSING PERSON', 'SECONDARY CODES', 'SUSPICIOUS OCC', 'FAMILY OFFENSES', 'LIQUOR LAWS', 'EXTORTION', 'LOITERING', 'TREA','BAD CHECKS']:
		df.loc[index, 'CrimeClass'] = 'OTHER CRIMES'


df.to_csv (r'C:\Users\parekh\Downloads\bytecamp\finalpolice.csv', index = None, header=True)