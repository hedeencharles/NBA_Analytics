from flask import Flask
from flask import render_template
import pymongo

# # Establish connection to local host 27017
# conn = 'mongodb://localhost:27017'

# # Connect to MongoClient
# client = pymongo.MongoClient(conn)



#create the Flask app


app = Flask(__name__)

#Create the Flask route for the index page
@app.route('/')
def index():
    return render_template("index.html")

#Create the Flask route for the about page
@app.route('/about')
def about():
    return render_template("about.html")

# # app route for api
# @app.route("/api/v1.0/nba_player_info")
# def players():
#     """Return player data as json"""
#     # Create session link for Python to DB
#     query = db.testing_beds.find_one()


# #Create the Flask route for the data page
# @app.route('/data', methods=['GET'])
# def data():
#     return '''<h1>NBA Player Birth Data</h1>
# <p>API for referencing NBA Player Birthplaces.</p>'''

# @app.route('/api/v1.0/player_data')
# def (player_data)

# @app.route('/data', methods=['GET'])
# def api_all():
#     return json.dumps(playerdata)


    # # Use a for loop to confirm data is now located in the database
    # all_players = []
    # for player in query:
    #     all_players.append(player)

    # return jsonify(all_results)
    
app.run(debug=True, port=5000)
