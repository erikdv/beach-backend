import os
from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

mongo_host = os.environ.get('BACKEND_MONGO_HOST')
mongo_db = os.environ.get('BACKEND_MONGO_DATABASE')

app.config['MONGO_DBNAME'] = mongo_db
app.config['MONGO_URI'] = 'mongodb://' + mongo_host + ':27017/' + mongo_db

mongo = PyMongo(app)

@app.route('/beach', methods=['GET'])
def get_all_beachs():
  beach = mongo.db.beachs
  output = []
  for s in beach.find():
    output.append({'name' : s['name'], 'rating' : s['rating']})
  return jsonify({'result' : output})

@app.route('/beach/', methods=['GET'])
def get_one_beach(name):
  beach = mongo.db.beachs
  s = beach.find_one({'name' : name})
  if s:
    output = {'name' : s['name'], 'rating' : s['rating']}
  else:
    output = "No such name"
  return jsonify({'result' : output})

@app.route('/beach', methods=['POST'])
def add_beach():
  beach = mongo.db.beachs
  name = request.json['name']
  rating = request.json['rating']
  beach_id = beach.insert({'name': name, 'rating': rating})
  new_beach = beach.find_one({'_id': beach_id })
  output = {'name' : new_beach['name'], 'rating' : new_beach['rating']}
  return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

