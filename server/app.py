# Web App implementation
# By: macdre

import logging
import os
import json
import connexion

from flask import jsonify
from flask_cors import CORS, cross_origin

from auth import requires_auth, AuthError
from models import db, PatientVitals
from sqlalchemy.orm import load_only

@cross_origin(headers=["Content-Type", "Authorization"])
@cross_origin(headers=["Access-Control-Allow-Origin", "http://localhost:5000"])
@requires_auth
def test():
    query_result = db.session.query(PatientVitals).all()
    return json.dumps([row.json() for row in query_result])

@cross_origin(headers=["Content-Type", "Authorization"])
@cross_origin(headers=["Access-Control-Allow-Origin", "http://localhost:5000"])
@requires_auth
def get_patient_vitals(user_id, quantity=1):
    query_result = db.session \
        .query(PatientVitals) \
        .filter(PatientVitals.user_id == user_id) \
        .order_by(PatientVitals.entry_date.desc()).limit(quantity).all()
    return json.dumps([row.json() for row in query_result])

@cross_origin(headers=["Content-Type", "Authorization"])
@cross_origin(headers=["Access-Control-Allow-Origin", "http://localhost:5000"])
@requires_auth
def post_patient_vitals(body):
    # new_patient_vitals = PatientVitals(body['patient_vitals']['user_id'],
    #                                    body['patient_vitals']['entry_date'],
    #                                    body['patient_vitals']['systolic_pressure'],
    #                                    body['patient_vitals']['diastolic_pressure'],
    #                                    body['patient_vitals']['weight_in_kg'])
    new_patient_vitals = PatientVitals(json.dumps(body['patient_vitals']))

    # Add the record to the session object
    db.session.add(new_patient_vitals)
    # commit the record the database
    db.session.commit()

    # do something
    return '201'

@cross_origin(headers=["Content-Type", "Authorization"])
@cross_origin(headers=["Access-Control-Allow-Origin", "http://localhost:5000"])
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
