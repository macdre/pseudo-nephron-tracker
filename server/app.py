# Web App implementation
# By: macdre

import logging
import os
import json
import connexion
import time
from flask import jsonify
from flask_cors import CORS, cross_origin
from marshmallow import exceptions as marsh_exceptions
from auth import requires_auth, AuthError
from models import db, PatientVitals, PatientVitalsSchema, EnrolledPatients, EnrolledPatientsSchema
from psycopg2 import errors as psy_errors
from sqlalchemy import exc as sqlalchemy_exceptions

@cross_origin()
@requires_auth
def test():
    query_result = db.session.query(PatientVitals).all()
    return json.dumps([PatientVitalsSchema().dump(row) for row in query_result])

@cross_origin()
@requires_auth
def delete_patient_vitals(user_id, entry_date):

    # First we need to make sure the user_id that is passed in is valid
    print("Got user_id: " + user_id)
    enrolled_query_result = db.session \
        .query(EnrolledPatients) \
        .filter(EnrolledPatients.user_id == user_id) \
        .limit(1).all()
    is_patient_enrolled = len(enrolled_query_result) > 0
    print("Is user enrolled? " + str(is_patient_enrolled))

    # Then we need to determine whether an entry for this date already exists
    try:
        vitals_query_result = db.session \
            .query(PatientVitals) \
            .filter(PatientVitals.user_id == user_id, PatientVitals.entry_date == entry_date) \
            .limit(1).all()
        does_entry_exist = len(vitals_query_result) > 0
        print("Does an entry already exist for this date? " + str(does_entry_exist))
    except (marsh_exceptions.ValidationError, sqlalchemy_exceptions.DataError) as e:
        print("Caught exception on delete: " + str(e))
        return "Caught exception on delete: " + str(e), 422

    # If user_id is valid and an entry exists, lets delete the entry
    if is_patient_enrolled:
        if does_entry_exist:  
            # We need to catch db errors and convert them into http return codes
            try:
                query_result = db.session \
                    .query(PatientVitals) \
                    .filter(PatientVitals.user_id == user_id, PatientVitals.entry_date == entry_date) \
                    .delete()
                db.session.commit()
            except (marsh_exceptions.ValidationError, sqlalchemy_exceptions.DataError) as e:
                print("Caught exception on delete: " + str(e))
                return "Caught exception on delete: " + str(e), 422

            # Then let's fetch the entry to ensure it was deleted
            vitals_query_result = db.session \
                .query(PatientVitals) \
                .filter(PatientVitals.user_id == user_id, PatientVitals.entry_date == entry_date) \
                .limit(1).all()
            does_entry_exist = len(vitals_query_result) > 0

            if not does_entry_exist:
                return "Delete Successful", 201
            else:
                print("Something went wrong trying to delete the record.")
                return "Something went wrong trying to delete the record.", 500
        else:
            print("There was no vital record for that date.")
            return "There was no vital record for that date.", 404
    else:
        print("The user_id is not enrolled.")
        return "The user_id is not enrolled.", 404
    
    # If we got here, something went wrong
    return "Something went wrong trying to parse the record to delete.", 500

@cross_origin()
@requires_auth
def get_patient_vitals(user_id, quantity=1):
    query_result = db.session \
        .query(PatientVitals) \
        .filter(PatientVitals.user_id == user_id) \
        .order_by(PatientVitals.entry_date.desc()).limit(quantity).all()
    # We need to catch db errors and convert them into http return codes
    return json.dumps([PatientVitalsSchema().dump(row) for row in query_result])

@cross_origin()
@requires_auth
def post_patient_vitals(body):
    print("Processing a request with body: " + str(body['patient_vitals']))

    # First we need to make sure the user_id that is passed in is valid
    user_id = body['patient_vitals']['user_id']
    print("Got user_id: " + user_id)
    enrolled_query_result = db.session \
        .query(EnrolledPatients) \
        .filter(EnrolledPatients.user_id == user_id) \
        .limit(1).all()
    is_patient_enrolled = len(enrolled_query_result) > 0
    print("Is user enrolled? " + str(is_patient_enrolled))

    # Then we need to determine whether an entry for this date already exists
    entry_date = body['patient_vitals']['entry_date']
    vitals_query_result = db.session \
        .query(PatientVitals) \
        .filter(PatientVitals.user_id == user_id, PatientVitals.entry_date == entry_date) \
        .limit(1).all()
    does_entry_exist = len(vitals_query_result) > 0
    print("Does an entry already exist for this date? " + str(does_entry_exist))
    
    # If user_id is valid and an entry doesn't exist, lets insert the request
    if is_patient_enrolled:
        if not does_entry_exist:  
            # We need to catch db errors and convert them into http return codes
            try:
                new_patient_vitals = PatientVitalsSchema().load(body['patient_vitals'], session=db.session)
                db.session.add(new_patient_vitals)
                db.session.commit()
            except marsh_exceptions.ValidationError as e:
                print("Caught exception on insert: " + str(e))
                return "Caught exception on insert: " + str(e), 422

            # Then let's fetch the entry to ensure it was saved
            vitals_query_result = db.session \
                .query(PatientVitals) \
                .filter(PatientVitals.user_id == user_id) \
                .limit(1).all()
            does_entry_exist = len(vitals_query_result) > 0

            if does_entry_exist:
                return "Insert Successful", 201
            else:
                print("Something went wrong trying to insert the record.")
                return "Something went wrong trying to insert the record.", 500
        else:
            print("There was already a vital record for that date.")
            return "There was already a vital record for that date.", 409
    else:
        print("The user_id is not enrolled.")
        return "The user_id is not enrolled.", 404
    
    # If we got here, something went wrong
    return "Something went wrong trying to parse the record to insert.", 500

@cross_origin()
@requires_auth
def patch_patient_vitals(PatientVitals):
    # do something
    return '200'

app = connexion.FlaskApp(__name__, specification_dir='swagger/')
app.add_api('swagger.yaml')
application = app.app
logging.basicConfig(level=logging.INFO)
CORS(application)
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db.init_app(application)

@application.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response

if __name__ == "__main__":
    context = ('./myserver.crt', './myserver.key')
    app.run(threading=True, ssl_context=context)
