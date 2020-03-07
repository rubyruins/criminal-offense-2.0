from flask import *
import pandas as pd
import numpy as np

app = Flask(__name__)

df = pd.read_csv("policefinal.csv")

@app.route('/')
def home():
	return render_template("home.html")

@app.route('/query')
def query():
	return render_template("query.html", crimeclasslen = len(df['CrimeClass'].unique()), uniquecrimeclass = df['CrimeClass'].unique(), districtlen = len(df['PdDistrict'].unique()), uniquedistrict = df['PdDistrict'].unique(), reslen = len(df['Resolution'].unique()), uniqueres = df['Resolution'].unique(), daylen = len(df['DayOfWeek'].unique()), uniquedays = df['DayOfWeek'].unique())

@app.route('/query', methods =['POST'])
def queryresult():
	crimeclass = request.form['usercrimeclass']
	district = request.form['userdistrict']
	resolution = request.form['userresolution']
	day = request.form['userday']
	department = request.form['userdepartment']
	incident = request.form['userincident']
	date = request.form['userdate']
	month = request.form['usermonth']
	time = request.form['usertime']
	print(time)
	print(type(time))
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
	if date:
		date = date.split("-")
		date = date[2] + "-" + date[1] + "-" + date[0]
		data = data[data['Date'] == str(date)]
	if month != '0':
		data = data[data['Month'] == int(month)]
	print(crimeclass, district, resolution, department, incident)
	print(data)
	data.reset_index(drop=True, inplace=True)
	datalength = len(data)
	if datalength == 0:
		template = "404.html"
	else:
		template = "queryresult.html"
	return render_template(template, datalength=datalength, data=data)


@app.route('/visualise')
def visualise():
	return render_template("visualise.html", crimeclasslen = len(df['CrimeClass'].unique()), uniquecrimeclass = df['CrimeClass'].unique(), districtlen = len(df['PdDistrict'].unique()), uniquedistrict = df['PdDistrict'].unique(), reslen = len(df['Resolution'].unique()), uniqueres = df['Resolution'].unique(), daylen = len(df['DayOfWeek'].unique()), uniquedays = df['DayOfWeek'].unique())

@app.route('/visualise', methods =['POST'])
def visualiseresult():
	crimeclass = request.form['usercrimeclass']
	district = request.form['userdistrict']
	resolution = request.form['userresolution']
	day = request.form['userday']
	department = request.form['userdepartment']
	incident = request.form['userincident']
	date = request.form['userdate']
	month = request.form['usermonth']
	time = request.form['usertime']
	print(time)
	print(type(time))
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
	if date:
		date = date.split("-")
		date = date[2] + "-" + date[1] + "-" + date[0]
		data = data[data['Date'] == str(date)]
	if month != '0':
		data = data[data['Month'] == int(month)]
	print(crimeclass, district, resolution, department, incident)
	print(data)
	data.reset_index(drop=True, inplace=True)
	datalength = len(data)
	if datalength == 0:
		template = "404.html"
	else:
		template = "visualiseresult.html"
		d = dict(data['CrimeClass'].value_counts())
		classlabels = list(d.keys())
		classvalues = list(d.values())
		maxclassvalue = max(classvalues)
		maxclasslabel = classlabels[classvalues.index(maxclassvalue)]
		maxclasspercentage = int(maxclassvalue * 100 / sum(classvalues))
		d = dict(data['PdDistrict'].value_counts())
		districtlabels = list(d.keys())
		districtvalues = list(d.values())
		maxdistrictvalue = max(districtvalues)
		maxdistrictlabel = districtlabels[districtvalues.index(maxdistrictvalue)]
		maxdistrictpercentage = int(maxdistrictvalue * 100 / sum(districtvalues))
		d = dict(data['Resolution'].value_counts())
		reslabels = list(d.keys())
		resvalues = list(d.values())
		maxresvalue = max(resvalues)
		maxreslabel = reslabels[resvalues.index(maxresvalue)]
		maxrespercentage = int(maxresvalue * 100 / sum(resvalues))
		d = dict(data['DayOfWeek'].value_counts())
		daylabels = list(d.keys())
		dayvalues = list(d.values())
		maxdayvalue = max(dayvalues)
		maxdaylabel = daylabels[dayvalues.index(maxdayvalue)]
		maxdaypercentage = int(maxdayvalue * 100 / sum(dayvalues))
	return render_template(template, datalength=datalength, classlabels=classlabels, classvalues=classvalues, maxclasslabel=maxclasslabel, maxclasspercentage=maxclasspercentage, districtlabels=districtlabels, districtvalues=districtvalues, maxdistrictvalue=maxdistrictvalue, maxdistrictlabel=maxdistrictlabel, maxdistrictpercentage=maxdistrictpercentage, reslabels=reslabels, resvalues=resvalues, maxresvalue=maxresvalue, maxreslabel=maxreslabel, maxrespercentage=maxrespercentage, daylabels=daylabels, dayvalues=dayvalues, maxdaylabel=maxdaylabel, maxdaypercentage=maxdaypercentage)

@app.errorhandler(404)
def error(e):
    return render_template("404.html")

if __name__ == "__main__":
	app.run(debug=True)