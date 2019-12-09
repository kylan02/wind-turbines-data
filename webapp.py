from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
	with open('wind_turbines.json') as turbine_data:
		turbines = json.load(turbine_data)
	return render_template('home.html')
	
def get_state_options(turbines):
	listOfStates = ['']
	for data in turbines:
		if data['Site']['State'] not in listOfStates:
			listOfStates.append(data['Site']['State'])
	options = ""
	for data in listOfStates:
		options = options + Markup("<option value=\""+data+"\">"+data+"</option>")
	return options
	
def get_rotor_sizes(turbines):
	listOfRotors = []
	for data in turbines:
		if data['Turbine']['Rotor_Diameter'] not in listOfRotors:
			listOfRotors.append(data['Turbine']['Rotor_Diameter'])
	listOfRotors.sort()
	options = ""
	for data in listOfRotors:
		options = options + Markup("<option value=\""+str(data)+"\">"+str(data)+"</option>")
	return options
	
def get_years(turbines):
	listOfYears = []
	for data in turbines:
		if data['Year'] not in listOfYears:
			listOfYears.append(data['Year'])
	listOfYears.sort()
	options = ""
	for data in listOfYears:
		options = options + Markup("<option value=\""+str(data)+"\">"+str(data)+"</option>")
	return options
	
def get_height(turbines):
	listOfHeights = []
	for data in turbines:
		if data['Turbine']['Hub_Height'] not in listOfHeights:
			listOfHeights.append(data['Turbine']['Hub_Height'])
	listOfHeights.sort()
	options = ""
	for data in listOfHeights:
		options = options + Markup("<option value=\""+str(data)+"\">"+str(data)+"</option>")
	return options
	
@app.route("/ByState")
def render_page1():
	with open('wind_turbines.json') as turbine_data:
		turbines = json.load(turbine_data)
	powerList = []
	if 'states' in request.args:
		for data in turbines:
			if data['Site']['State'] == request.args['states']:
				powerList.append(data['Turbine']['Capacity'])
		average = sum(powerList) / len(powerList)
		return render_template('state.html', states = get_state_options(turbines), averageKW = average, state = request.args['states'])
	else: return render_template('state.html', states = get_state_options(turbines))
	
@app.route("/ByRotorSize")
def render_page2():
	with open('wind_turbines.json') as turbine_data:
		turbines = json.load(turbine_data)
	powerList = []
	if 'rotorSize' in request.args:
		for data in turbines:
			if float(data['Turbine']['Rotor_Diameter']) == float(request.args['rotorSize']):
				powerList.append(data['Turbine']['Capacity'])
		average = sum(powerList) / len(powerList)
		return render_template('rotor.html', rotorSize = get_rotor_sizes(turbines), averageKW = average, rotor = request.args['rotorSize'])
	else: return render_template('rotor.html', rotorSize = get_rotor_sizes(turbines))
	
@app.route("/ByYear")
def render_page3():
	with open('wind_turbines.json') as turbine_data:
		turbines = json.load(turbine_data)
	powerList = []
	if 'year' in request.args:
		for data in turbines:
			if int(data['Year']) == int(request.args['year']):
				powerList.append(data['Turbine']['Capacity'])
		average = sum(powerList)/ len(powerList)
		return render_template('year.html', year = get_years(turbines), averageKW = average, selectedYear = request.args['year'])
	else: return render_template('year.html', year = get_years(turbines))
	
@app.route("/ByHeight")
def render_page4():
	with open('wind_turbines.json') as turbine_data:
		turbines = json.load(turbine_data)
	powerList = []
	if 'height' in request.args:
		for data in turbines:
			if float(data['Turbine']['Hub_Height']) == float(request.args['height']):
				powerList.append(data['Turbine']['Capacity'])
		average = sum(powerList)/ len(powerList)
		return render_template('height.html', height = get_height(turbines), averageKW = average, selectedHeight = request.args['height'])
	else: return render_template('height.html', height = get_height(turbines))
	
if __name__=="__main__":
    app.run(debug=False)