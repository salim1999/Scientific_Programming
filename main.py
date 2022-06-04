from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import requests;

import matplotlib as mpl

import pandas as pd

import csv

app = Flask(__name__)
app.debug = True


@app.route("/type", methods=['GET', 'POST'])
def createplot():
    file = 'Ukraine_war.csv'
    if file != '':
        print(request.values["drone"])

        with open(file) as csvfile:
            data = pd.read_csv("ukraine_war.csv")
            if request.values["drone"]=="true":
                x1 = data["drone"]
                plt.plot(x1, color='red', label='drone')

            if request.values["aircraft"]=="true":
                x2 = data["aircraft"]
                plt.plot(x2, color='green', label='aircraft')

            if request.values["helicopter"]=="true":
                x3 = data["helicopter"]
                plt.plot(x3, color='olive', label='helicopter')

            if request.values["tank"]=="true":
                x4 = data["tank"]
                plt.plot(x4, color='blue', label='tank')

            plt.legend()
            plt.ylabel('lost Military Equipement')
            plt.xlabel('number of days')
            plt.savefig('static/Output.jpg', bbox_inches='tight', dpi=150)
            plt.close()
    return ""

@app.route("/")
def home():
    return render_template('home.html')

