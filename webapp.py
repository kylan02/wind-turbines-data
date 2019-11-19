from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
	with open('wind_turbines.json') as turbine_data:
		counties = json.load(turbine_data)
	return render_template('home.html')
	
@app.route("/ByState")
def render_page1():
	return render_template('state.html')
	
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