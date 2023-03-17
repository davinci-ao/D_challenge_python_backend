import json
from flask import Flask, jsonify, url_for, request
from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

class PersonSchema(Schema):
    name = fields.Str()
    firstName = fields.Str()
    age = fields.Integer()
    

person = dict(name="Bond", firstName="James", age=55)
personSchema = PersonSchema()

# default route
@app.route('/', methods=["GET"])
def index():
    return jsonify({'data': 'Everything is working as expected!',
                    'error': False,
                    'error_msg': ''})


# get person route
@app.route('/person', methods=["GET"])
def getPerson():
    return jsonify({'data': personSchema.dump(person),
                    'error': False,
                    'error_msg': ''})

# routes for updating
@app.route('/person/update', methods=["POST"])
def updatePerson():
    try:
        # get fields from post request
        data = request.json["data"]
        # set fields in global object
        person.name = data.name
        person.firstName = data.firstName
        person.age = data.age
       
        return jsonify({'data': personSchema.dump(person),
                        'error': False,
                        'error_msg': ''})
    except Exception as e:
        return jsonify({'data': '',
                        'error': True,
                        'error_msg': str(e)})

app.run(host='0.0.0.0', port=5000, debug=True)