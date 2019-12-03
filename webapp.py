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
		print(request.args['rotorSize'])
		for data in turbines:
			if data['Turbine']['Rotor_Diameter'] == request.args['rotorSize']:
				powerList.append(data['Turbine']['Capacity'])
				print("if is true")
		print(powerList)
		average = sum(powerList) / len(powerList)
		return render_template('rotor.html', rotorSize = get_rotor_sizes(turbines), averageKW = average, rotor = request.args['rotorSize'])
	else: return render_template('rotor.html', rotorSize = get_rotor_sizes(turbines))
	
@app.route("/ByYear")
def render_page3():
	return render_template('year.html')
	
@app.route("/ByHeight")
def render_page4():
	return render_template('height.html')
	
if __name__=="__main__":
    app.run(debug=False)