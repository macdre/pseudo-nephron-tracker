# This is by me!

from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

db = SQLAlchemy()

class PatientVitals(db.Model):
    # Model for the patient_vital_history table
    __tablename__ = 'patient_vital_history'
    __table_args__ = {'quote':False}
    user_id = db.Column('user_id', db.Text, primary_key=True)
    entry_date = db.Column('entry_date', db.Date, primary_key=True)
    systolic_pressure = db.Column('systolic_pressure', db.Integer)
    diastolic_pressure = db.Column('diastolic_pressure', db.Integer)
    weight_in_kg = db.Column('weight_in_kg', db.Float)
    initial_drain = db.Column('initial_drain', db.Integer)
    total_uf = db.Column('total_uf', db.Integer)
    average_dwell = db.Column('average_dwell', db.Text)
    added_lost_dwell_type = db.Column('added_lost_dwell_type', db.Text)
    added_lost_dwell_value = db.Column('added_lost_dwell_value', db.Text)
    drain_color = db.Column('drain_color', db.Text)
    drain_clarity = db.Column('drain_clarity', db.Text)
    fibrin_present = db.Column('fibrin_present', db.Text)
    exit_color = db.Column('exit_color', db.Text)
    exit_sensitivity = db.Column('exit_sensitivity', db.Text)
    exit_condition = db.Column('exit_condition', db.Text)
    bowel_obs = db.Column('bowel_obs', db.Text)
    treatment_problems = db.Column('treatment_problems', db.Text)
    comments = db.Column('comments', db.Text)

class PatientVitalsSchema(SQLAlchemySchema):
    class Meta:
        model = PatientVitals
        load_instance = True  # Optional: deserialize to model instances
    user_id = auto_field()
    entry_date = auto_field()
    systolic_pressure = auto_field()
    diastolic_pressure = auto_field()
    weight_in_kg = auto_field()
    initial_drain =auto_field()
    total_uf = auto_field()
    average_dwell = auto_field()
    added_lost_dwell_type = auto_field()
    added_lost_dwell_value = auto_field()
    drain_color = auto_field()
    drain_clarity = auto_field()
    fibrin_present = auto_field()
    exit_color = auto_field()
    exit_sensitivity = auto_field()
    exit_condition = auto_field()
    bowel_obs = auto_field()
    treatment_problems = auto_field()
    comments = auto_field()

class EnrolledPatients(db.Model):
    # Model for the enrolled_patients table
    __tablename__ = 'enrolled_patients'
    __table_args__ = {'quote':False}
    user_id = db.Column('user_id', db.Text, primary_key=True)
    enrolled_date = db.Column('enrolled_date', db.Date)

class EnrolledPatientsSchema(SQLAlchemySchema):
    class Meta:
        model = EnrolledPatients
        load_instance = True  # Optional: deserialize to model instances
    user_id = auto_field()
    enrolled_date = auto_field()