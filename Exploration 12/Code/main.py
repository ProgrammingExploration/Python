from flask import Flask, jsonify
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite://database.db'
db = SQLAlchemy(app)

@app.route('/')
def home():
    return 'Hi'

class Home(Resource):
    def get(self):
        return '<h1>Youtube API</h1>'
    
    def post(self):
        return "<h1>Post Request</h1>"

api.add_resource(Home, '/home')

app.run(port=5000)
