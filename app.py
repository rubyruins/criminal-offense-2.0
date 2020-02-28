from flask import *
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

app = Flask(__name__)

df = pd.read_csv("policefinal.csv")

@app.route('/')
def home():
	return render_template("index.html", crimeclasslen = len(df['CrimeClass'].unique()), uniquecrimeclass = df['CrimeClass'].unique(), districtlen = len(df['PdDistrict'].unique()), uniquedistrict = df['PdDistrict'].unique(), reslen = len(df['Resolution'].unique()), uniqueres = df['Resolution'].unique(), daylen = len(df['DayOfWeek'].unique()), uniquedays = df['DayOfWeek'].unique())

@app.route('/', methods =['POST'])
def basic():
	crimeclass = request.form['usercrimeclass']
	district = request.form['userdistrict']
	resolution = request.form['userresolution']
	day = request.form['userday']
	department = request.form['userdepartment']
	incident = request.form['userincident']
	data = df.copy(deep = True)
	if crimeclass != '0':
		data = data[data['CrimeClass'] == crimeclass]
	if district != '0':
		data = data[data['PdDistrict'] == district]
	if resolution != '0':
		data = data[data['Resolution'] == resolution]
	if day != '0':
		data = data[data['DayOfWeek'] == day]
	if department != '0':
		data = data[data['PdId'] == int(department)]
	if incident != '0':
		data = data[data['IncidntNum'] == int(incident)]
	print(crimeclass, district, resolution, department, incident)
	print(data)
	data.reset_index(drop=True, inplace=True)
	datalength = len(data)
	if datalength == 0:
		template = "404.html"
	else:
		template = "tables.html"
		d = dict(data['CrimeClass'].value_counts())
		classlabels = list(d.keys())
		classvalues = list(d.values())
		d = dict(data['PdDistrict'].value_counts())
		districtlabels = list(d.keys())
		districtvalues = list(d.values())
		maxdistrictvalue = max(districtvalues)
		d = dict(data['Resolution'].value_counts())
		reslabels = list(d.keys())
		resvalues = list(d.values())
		maxresvalue = max(resvalues)
		d = dict(data['DayOfWeek'].value_counts())
		daylabels = list(d.keys())
		dayvalues = list(d.values())
	return render_template(template, datalength=datalength, data=data, classlabels=classlabels, classvalues=classvalues, districtlabels=districtlabels, districtvalues=districtvalues, maxdistrictvalue=maxdistrictvalue, reslabels=reslabels, resvalues=resvalues, maxresvalue=maxresvalue, daylabels=daylabels, dayvalues=dayvalues)

@app.errorhandler(404)
def error(e):
    return render_template("404.html")

if __name__ == "__main__":
	app.run(debug=True)