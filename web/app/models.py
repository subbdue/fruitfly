from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True)

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sensorid = db.Column(db.Integer, index=True)
    location = db.Column(db.Integer, index=True)

    def __repr__(self):
        return '<Sensor %r>' % (self.sensorid)

class Reading(db.Model):
    __Searchable__ = ['timestamp']

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)
    value = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('sensor.id'))

    def __repr__(self):  # pragma: no cover
        return '<Reading %r>' % (self.value)

