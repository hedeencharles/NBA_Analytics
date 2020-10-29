from flask import Flask
from flask import render_template

import csv
import json

#Read in the Plyaer Birth csv
with open ('../Datasets/Players.csv', newline='') as csvfile:
     playerdata = csv.reader(csvfile, delimiter=' ', quotechar='|')
    #  for row in playerdata:
        #  print(row)

#Convert the csv to JSON
playerdata = json.dumps(playerdata)

#create the Flask app
app = Flask(__name__)

#Create the Flask route for the index page
@app.route('/index')
def index():
    return render_template("index.html")

#Create the Flask route for the about page
@app.route('/about')
def about():
    return render_template("about.html")


#Create the Flask route for the data page
@app.route('/data', methods=['GET'])
def data():
    return '''<h1>NBA Player Birth Data</h1>
<p>API for referencing NBA Player Birthplaces.</p>'''

@app.route('/api/v1.0/player_data')
def (player_data)

# @app.route('/data', methods=['GET'])
# def api_all():
#     return json.dumps(playerdata)


app.run(debug=True, port=5000)
