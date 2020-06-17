# This is by me!

import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BaseModel(db.Model):
    # Base data model for all objects
    __abstract__ = True

    def __repr__(self):
        # Define a base way to print models
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self._to_dict().items()
        })

    def json(self):
        # Define a base way to jsonify models, dealing with datetime objects
        return {
            column: value if not isinstance(value, datetime.date) else value.strftime('%Y-%m-%d')
            for column, value in self._to_dict().items()
        }

class PatientVitals(BaseModel, db.Model):
    # Model for the patient_vital_histor table
    __tablename__ = 'patient_vital_history'
    __table_args__ = {'quote':False}
    user_id = db.Column('user_id', db.Integer, primary_key=True)
    entry_date = db.Column('entry_date', db.Date, primary_key=True)
    systolic_pressure = db.Column('systolic_pressure', db.Integer)
    diastolic_pressure = db.Column('diastolic_pressure', db.Integer)
    weight_in_kg = db.Column('weight_in_kg', db.Float)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'user_id'            : self.user_id,
            'entry_date'         : self.entry_date,
            'systolic_pressure'  : self.systolic_pressure,
            'diastolic_pressure' : self.diastolic_pressure,
            'weight_in_kg'       : self.weight_in_kg
        }
