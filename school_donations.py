from flask import Flask
from flask import render_template
from pymongo import MongoClient
import json

app = Flask(__name__)

MONGOD_HOST = 'ds025603.mlab.com'
MONGOD_PORT = 25603

DBS_NAME = 'heroku_0fwl2k35'
MONGO_URI = 'mongodb://root:rootpassword@ds025603.mlab.com:25603/heroku_0fwl2k35'
COLLECTION_NAME = 'projects'
FIELDS = {'funding_status': True, 'school_state': True, 'resource_type': True,
          'poverty_level': True, 'date_posted': True, 'total_donations': True, '_id': False}


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/donorsUS/projects")
def donor_projects():
    connection = MongoClient(MONGO_URI)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    projects = collection.find(projection=FIELDS, limit=20000)
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects)
    connection.close()
    return json_projects


if __name__ == "__main__":
    app.run(debug=True)
