# Imports
from flask import Flask,jsonify,redirect
from team import teams

# Settings
portApp = 4500

# Init app
app = Flask(__name__)

# Routes

# Initial Route (Get all Teams)
@app.route('/')
def init():
	return redirect("/teams")
@app.route('/teams')
def getTeams():
	return jsonify({"teams":teams,"author":"Damian Zsiros","Author web":"https://damian-zsiros.herokuapp.com/"})
# Get Teams by Name
@app.route('/teams/<string:team_name>')
def getTeamsByName(team_name):
	print(team_name)
	teamFound = [team for team in teams if team['name'].lower() == team_name]
	if (len(teamFound) > 0):
		return jsonify({"Teams founded":teamFound[0],"author":"Damian Zsiros","Author web":"https://damian-zsiros.herokuapp.com/"})
	return jsonify({"message":"Teams with the name '"+team_name+"' not found","author":"Damian Zsiros","Author web":"https://damian-zsiros.herokuapp.com/"})
# Post team
@app.route('/teams',methods=['POST'])
def postTeam():
	new_team = {
		"name":request.json['name'],
		"date_creation":request.json['date_creation'],
		"actual_president":request.json['actual_president']
	},
	teams.append(new_team)
	return jsonify({"message":"Team added succesfully","teams":teams,"author":"Damian Zsiros","Author web":"https://damian-zsiros.herokuapp.com/"})

# Edit team
@app.route('/teams/<string:team_name>',methods=['PUT'])
def editTeam(team_name):
	teamFound = [team for team in teams if team['name'].lower() == team_name]
	if (len(teamFound) > 0):
		teamFound[0]['name'] = request.json['name']
		teamFound[0]['date_creation'] = request.json['date_creation']
		teamFound[0]['actual_president'] = request.json['actual_president']
		return jsonify({"message":"Team "+team_name+" updated succesfully","teams":teams,"author":"Damian Zsiros","Author web":"https://damian-zsiros.herokuapp.com/"})

	return jsonify({"message":"Teams with the name '"+team_name+"' not found","author":"Damian Zsiros","Author web":"https://damian-zsiros.herokuapp.com/"})

# Delete team
@app.route('/teams/<string:team_name>',methods=['DELETE'])
def deleteTeam(team_name):
	teamFound = [team for team in teams if team['name'].lower() == team_name]
	if (len(teamFound) > 0):
		teams.remove(teamFound)
		return jsonify({"message":"Team "+team_name+" deleted succesfully","teams":teams,"author":"Damian Zsiros","Author web":"https://damian-zsiros.herokuapp.com/"})

	return jsonify({"message":"Teams with the name '"+team_name+"' not found","author":"Damian Zsiros","Author web":"https://damian-zsiros.herokuapp.com/"})

# Starting server
if (__name__ == '__main__'):
	app.run(debug=True,port=portApp)  

# Created by Damian Zsiros
# Web link: https://damian-zsiros.herokuapp.com/