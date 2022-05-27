from flask import Flask, render_template
import matplotlib.pyplot as plt

import matplotlib as mpl

import pandas as pd

import csv

app = Flask(__name__)
app.debug = True


@app.route("/")
def hello_world():
    file = 'Ukraine_war.csv'
    if file != '':
        with open(file) as csvfile:
            reader = csv.DictReader(csvfile)

            # count = 0

            # Read  the data from .csv-file

            data = pd.read_csv("ukraine_war.csv")

            x = data["personnel"]

            x2 = data["helicopter"]

            x3 = data["aircraft"]

            x4 = data["tank"]

            x5 = data["drone"]

            # plt.plot(x)

            plt.plot(x2, color='olive', label='helicopter')

            plt.plot(x3, color='green', label='aircraft')

            plt.plot(x4, color='blue', label='tank')

            plt.plot(x5, color='red', label='drone')
            plt.legend()
            plt.ylabel('lost Military Equipement')
            plt.xlabel('number of days')


            plt.savefig('static/Output.jpg', bbox_inches='tight', dpi=150)

    return render_template('home.html')
