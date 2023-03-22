# import de benodigde packages
from flask import Flask, jsonify, abort, request
from flask_cors import CORS
from procesData import *

# variables
# Dit maakt een nieuwe Flask app aan.
app = Flask(__name__)

# functions
# Default GET methode, geeft een string terug dat alles werkt zoals gewenst.
@app.route('/', methods=["GET"])
def index():
    return 'Everything is working as expected!'

# Write order to JSON file. Normally, you should write to a database.
@app.route('/order/create', methods=["POST"])
def createOrder():
    resp = jsonify(success=True)
    resp.status_code = 201

    # get data from post request
    data = request.get_json(force=True)
    try:
        writeOrder(data)
    except ValueError as e:
        resp = jsonify(str(e))
        resp.status_code = 400

    # en geef response terug
    return resp


# opvragen_order
@app.route('/order/get', methods=["GET"])
def returnOrder():
    # dit is een query parameter
    orderId = request.args.get('orderId')
    try:
        order = getOrder(orderId)
    except ValueError as e:
        resp = jsonify(str(e))
        resp.status_code = 400
        return resp

    resp = jsonify(str(order))
    return resp

# krijg factuur van order
@app.route('/order/invoice', methods=["GET"])
def getInvoice():
    # dit is een query parameter
    orderId = request.args.get('orderId')
    # De functie generateInvoice wordt aangeroepen, deze functie moet je aanpassen.
    invoice = generateInvoice(orderId)
    resp = jsonify(str(invoice))
    return resp


# code
CORS(app)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
