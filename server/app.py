# Web App implementation
# By: macdre

import logging
import os
import connexion

from flask import jsonify
from flask_cors import CORS, cross_origin

from auth import requires_auth, AuthError
from models import db, PatientVitals

@cross_origin(headers=["Content-Type", "Authorization"])
@cross_origin(headers=["Access-Control-Allow-Origin", "http://localhost:5000"])
@requires_auth
def test():
    query_result = db.session.query(PatientVitals).all()
    return jsonify(json_list=[i.serialize() for i in query_result])

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
