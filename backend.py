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

@app.route('/car', methods=['GET'])
def get_all_cars():
  car = mongo.db.cars
  output = []
  for s in car.find():
    output.append({'name' : s['name'], 'price' : s['price']})
  return jsonify({'result' : output})

@app.route('/car/', methods=['GET'])
def get_one_car(name):
  car = mongo.db.cars
  s = car.find_one({'name' : name})
  if s:
    output = {'name' : s['name'], 'price' : s['price']}
  else:
    output = "No such name"
  return jsonify({'result' : output})

@app.route('/car', methods=['POST'])
def add_car():
  car = mongo.db.cars
  name = request.json['name']
  price = request.json['price']
  car_id = car.insert({'name': name, 'price': price})
  new_car = car.find_one({'_id': car_id })
  output = {'name' : new_car['name'], 'price' : new_car['price']}
  return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

