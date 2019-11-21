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
	
@app.route("/ByState")
def render_page1():
	with open('wind_turbines.json') as turbine_data:
		turbines = json.load(turbine_data)
	powerList = []
	if 'states' in request.args:
		for data in turbines:
			if data['Site']['State'] == request.args['state']:
				powerList.append(data['Turbine']['Capacity'])
		average = sum(powerList) / len(powerList)
		return render_template('state.html', states = get_state_options(turbines), averageKW = average)
	else: return render_template('state.html', states = get_state_options(turbines))
	
@app.route("/ByRotorSize")
def render_page2():
	return render_template('rotor.html')
	
@app.route("/ByYear")
def render_page3():
	return render_template('year.html')
	
@app.route("/ByHeight")
def render_page4():
	return render_template('height.html')
	
if __name__=="__main__":
    app.run(debug=False)