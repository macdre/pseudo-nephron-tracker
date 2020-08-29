# This is by me!

import datetime
import json
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BaseModel(db.Model):
    # Base data model for all objects
    __abstract__ = True

    def __init__(self, data):
        self.__dict__ = json.loads(data) # TODO: this is overridding the orm vars, need to redo this

    def json(self):
        # Define a base way to jsonify models, dealing with datetime objects
        d = {}
        for column in self.__table__.columns:
            attr = getattr(self, column.name)
            if isinstance(attr, datetime.date):
                d[column.name] = attr.strftime('%Y-%m-%d')
            else:
                d[column.name] = str(getattr(self, column.name))
        return d

class PatientVitals(BaseModel, db.Model):
    # Model for the patient_vital_histor table
    __tablename__ = 'patient_vital_history'
    __table_args__ = {'quote':False}
    user_id = db.Column('user_id', db.Text, primary_key=True)
    entry_date = db.Column('entry_date', db.Date, primary_key=True)
    systolic_pressure = db.Column('systolic_pressure', db.Integer)
    diastolic_pressure = db.Column('diastolic_pressure', db.Integer)
    weight_in_kg = db.Column('weight_in_kg', db.Float)