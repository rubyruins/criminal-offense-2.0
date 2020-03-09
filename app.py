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
	return render_template("index.html", target="/query", crimeclasslen = len(df['CrimeClass'].unique()), uniquecrimeclass = df['CrimeClass'].unique(), districtlen = len(df['PdDistrict'].unique()), uniquedistrict = df['PdDistrict'].unique(), reslen = len(df['Resolution'].unique()), uniqueres = df['Resolution'].unique(), daylen = len(df['DayOfWeek'].unique()), uniquedays = df['DayOfWeek'].unique())

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
	if time:
		data = data[data['Time'] == str(time)]
	data.reset_index(drop=True, inplace=True)
	datalength = len(data)
	if datalength == 0:
		template = "404.html"
	else:
		template = "queryresult.html"
	return render_template(template, datalength=datalength, data=data)


@app.route('/visualise')
def visualise():
	return render_template("index.html", target="/visualise", crimeclasslen = len(df['CrimeClass'].unique()), uniquecrimeclass = df['CrimeClass'].unique(), districtlen = len(df['PdDistrict'].unique()), uniquedistrict = df['PdDistrict'].unique(), reslen = len(df['Resolution'].unique()), uniqueres = df['Resolution'].unique(), daylen = len(df['DayOfWeek'].unique()), uniquedays = df['DayOfWeek'].unique())

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
	if time:
		data = data[data['Time'] == str(time)]
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

		d = dict(data['Month'].value_counts())
		monthvalues = []
		for x in range(1,13):
			monthvalues.append(d.get(x, 0))
		monthlabels = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']
		maxmonthvalue = max(monthvalues)
		maxmonthlabel = monthlabels[monthvalues.index(maxmonthvalue)]
		maxmonthpercentage = int(maxmonthvalue * 100 / sum(monthvalues))

		d = dict(data['SingleDate'].value_counts())
		singledatelabels = []
		singledatevalues = []
		for i in sorted(d):
			singledatelabels.append(i)
			singledatevalues.append(d[i])
		maxsingledatevalue = max(singledatevalues)
		maxsingledatelabel = singledatelabels[singledatevalues.index(maxsingledatevalue)]
		maxsingledatepercentage = int(maxsingledatevalue * 100 / sum(singledatevalues))

		d = dict(data['Time'].value_counts())
		timelabels = []
		timevalues = []
		for i in sorted(d):
			timelabels.append(i)
			timevalues.append(d[i])
		maxtimevalue = max(timevalues)
		maxtimelabel = timelabels[timevalues.index(maxtimevalue)]
		maxtimepercentage = int(maxtimevalue * 100 / sum(timevalues))

	return render_template(template, datalength=datalength, classlabels=classlabels, classvalues=classvalues, maxclasslabel=maxclasslabel, maxclasspercentage=maxclasspercentage, districtlabels=districtlabels, districtvalues=districtvalues, maxdistrictvalue=maxdistrictvalue, maxdistrictlabel=maxdistrictlabel, maxdistrictpercentage=maxdistrictpercentage, reslabels=reslabels, resvalues=resvalues, maxresvalue=maxresvalue, maxreslabel=maxreslabel, maxrespercentage=maxrespercentage, daylabels=daylabels, dayvalues=dayvalues, maxdaylabel=maxdaylabel, maxdaypercentage=maxdaypercentage, monthlabels=monthlabels, monthvalues=monthvalues, maxmonthvalue=maxmonthvalue, maxmonthlabel=maxmonthlabel, maxmonthpercentage=maxmonthpercentage, singledatelabels=singledatelabels, singledatevalues=singledatevalues, maxsingledatevalue=maxsingledatevalue, maxsingledatelabel=maxsingledatelabel, maxsingledatepercentage=maxsingledatepercentage, timelabels=timelabels, timevalues=timevalues, maxtimevalue=maxtimevalue, maxtimelabel=maxtimelabel, maxtimepercentage=maxtimepercentage)


@app.route('/detail', methods=['POST'])
def detail():
	usersr = request.form['usersr']
	selected = df[df['SrNo'] == int(usersr)]
	incidntnum = int(selected['IncidntNum'])
	category = str(selected['Category'].item())
	descript = str(selected['Descript'].item())
	day = str(selected['DayOfWeek'].item())
	date = str(selected['Date'].item())
	district = str(selected['PdDistrict'].item())
	res = str(selected['Resolution'].item())
	add = str(selected['Address'].item())
	x = float(selected['X'])
	y = float(selected['Y'])
	pdid = int(selected['PdId'])
	crimeclass = str(selected['CrimeClass'].item())
	time = str(selected['Time'].item())
	return render_template("detail.html", usersr=usersr, incidntnum=incidntnum, category=category, descript=descript, day=day, date=date, district=district, res=res, add=add, x=x, y=y, pdid=pdid, crimeclass=crimeclass, time=time)

@app.errorhandler(404)
def error(e):
    return render_template("404.html")

if __name__ == "__main__":
	app.run(debug=True)