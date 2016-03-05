from flask import render_template, request
from app import app, db
from .models import User, Sensor, Reading
import json
import logging

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', title='Hello')

@app.route('/users', methods=['GET'])
def read():
    users = User.query.all()
    app.logger.info(users)
    return render_template('users.html', users=users)

@app.route('/users', methods=['POST'])
def write():
    if not request.json or not 'nickname' in request.json:
        abort(400)
    user = User(nickname=request.json['nickname'], email=request.json['email'])
    db.session.add(user)
    db.session.commit()
    users = User.query.all()
    return render_template('users.html', users=users), 201

@app.route('/sensors', methods=['GET'])
def sensor_read():
    app.logger.info('Info')
    sensors = Sensor.query.all()
    app.logger.info(sensors)
    return render_template('sensors.html', sensors=sensors)

@app.route('/sensors', methods=['POST'])
def sensor_write():
    if not request.json:
        abort(400)
    sensor = Sensor(sensorid=request.json['sensorid'], location=request.json['location'])
    db.session.add(sensor)
    db.session.commit()
    sensors = Sensor.query.all()
    return render_template('sensors.html', sensors=sensors), 201

@app.route('/readings', methods=['GET'])
def readings_read():
    app.logger.info('Info')
    readings = Reading.query.all()
    app.logger.info(readings)
    return render_template('readings.html', readings=readings)

@app.route('/readings', methods=['POST'])
def readings_write():
    if not request.json:
        abort(400)
    reading = Reading(timestamp=request.json['timestamp'], value=request.json['value'])
    db.session.add(reading)
    db.session.commit()
    readings = Reading.query.all()
    return render_template('readings.html', readings=readings), 201
