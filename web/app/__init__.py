from flask import Flask, jsonify, request
from flask.ext.sqlalchemy import SQLAlchemy
import logging

app = Flask(__name__)
app.config.from_object('config')
app.config['DEBUG'] = True
db = SQLAlchemy(app)

floors = [
    {
        'id': 1,
        'status': 0,
        'weight': 0,
        'time': ["9:00", "12:00"]
        
    },
    {
        'id': 2,
        'status': 0,
        'weight': 0,
        'time': ["9:00", "9:10"]
    },
    {
        'id': 3,
        'status': "AVAIL",
        'weight': 39,
        'time': ["9:00", "11:10"]
    }
]

@app.route('/floors', methods=['GET'])
def get_floor():
    return jsonify({'floors': floors})

@app.route('/floors', methods=['POST'])
def create_task():
    if not request.json or not 'id' in request.json:
        abort(400)
    sensorid = request.json['id']-1
    app.logger.info(floors[sensorid])
    app.logger.info(floors[sensorid]['weight'])
    app.logger.info(request.json['weight'])

    if floors[sensorid]['weight']  == 0 and request.json['weight'] > 0:
        # 0 - 1 transition, update entry
        floors[sensorid]['time'][0] = request.json['time']
        floors[sensorid]['status'] = 1

    if floors[sensorid]['weight'] > 0 and request.json['weight'] == 0:
        # 1 - 0 transition, update entry
        floors[sensorid]['time'][1] = request.json['time']
        floors[sensorid]['status'] = 0

    # always update weight
    floors[sensorid]['weight'] = request.json['weight']

    return jsonify({'floors': floors}), 201

from app import views, models
