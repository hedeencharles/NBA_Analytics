from flask import Flask
from flask import render_template
#import pymongo

# # Establish connection to local host 27017
# conn = 'mongodb://localhost:27017'

# # Connect to MongoClient
# client = pymongo.MongoClient(conn)

# app.config["MONGO_URI"] = 'mongodb://localhost:27017'

# mongo = Pymongo(app)
# servicerequests = mongo.dv.servicerequests

#create the Flask app
app = Flask(__name__)
# CORS(app)

#Create the Flask route for the index page
@app.route('/')
def index():
    return render_template("index.html")

#Create the Flask route for the about page
@app.route('/api')
def api():
    return render_template("api.html")

# app route for graph 1
@app.route("/graph1")
def graph1():
    return render_template("graph1.html")
   # Create session link for Python to DB
   # query = db.testing_beds.find_one()

#@app.route("/api/v1/data", methods=['GET'])
#def serveData():
 #   return jsonify(list(servicerequests.find({ },
  # { '_id': 0})))


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


<<<<<<< HEAD
    # # Use a for loop to confirm data is now located in the database
=======
#<<<<<<< HEAD
    # # Use a for loop to confirm data is now located in the database
#=======
    # Use a for loop to confirm data is now located in the database
    #all_players = []
    #for player in query:
     #   all_players.append(player)

   # return jsonify(all_results)
#>>>>>>> 9556a60ec5444ce7bee787322dfc894bb8bc0787
>>>>>>> 074573905bb7a934789d22f55211261eb17b6951
    # all_players = []
    # for player in query:
    #     all_players.append(player)

    # return jsonify(all_results)
    
app.run(debug=True, port=5000)
