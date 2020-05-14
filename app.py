# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: laceystrahm
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static default home route
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/1006assignments")
def ENGI_1006_Assignments():
    #has to be in templates folder to render html
    return render_template("1006assignments.html")

@app.route("/ISC")
def Information_Science_Courses():
    return render_template("InformationScienceCourses.html")

#start the server
if __name__ == "__main__":
    app.run()
