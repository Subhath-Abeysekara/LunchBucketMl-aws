# This is a sample Python script
import json

import numpy as np
import writeCsv as w
import readCsv as r


#import flask library for build apis
from flask import Flask,request, jsonify
#flask cors handing
from flask_cors import CORS , cross_origin



import pickle

app = Flask(__name__)
#enable cross origin for any ip
CORS(app , resources={r"/":{"origins":"*"}})

#Home Api
@app.route("/")
def main():
    return "hello world"

#First Page
@app.route("/home")
@cross_origin()
def home():
    return "First Page"

#Api for create csv file
@app.route("/initCsv" , methods = ["GET"])
@cross_origin()
def model():

    w.csv_start()

    return "success"

# Api for change price of a packet
@app.route("/updatePrice", methods=["GET"])
@cross_origin()
def model1():
    # get rating value as api parameter
    price = request.args.get('price')
    print('price ' + price)

    w.change_price(price)
    print(w.price)
    return "success"



# Api for  add data row to csv
@app.route("/addDataCsv", methods=["GET"])
@cross_origin()
def model2():
    # get rating value as api parameter
    packets = request.args.get('packet')
    print('packets ' + packets)

    w.csv_write_new_row(int(packets))

    return "success"

# Api for change offer id
@app.route("/updateOfferId", methods=["GET"])
@cross_origin()
def model3():
    # get rating value as api parameter
    id = request.args.get('id')
    print('id ' + id)

    w.set_offer_id(id)

    return "success"

# Api for get best offer
@app.route("/getOffer", methods=["GET"])
@cross_origin()
def model4():

    return r.check_best_offer()

@app.route("/getDetails", methods=["GET"])
@cross_origin()
def model5():

    return {
        "price" : w.price,
        "yestertay revenue":w.yesterday_revenue,
        "yesterday offer" : w.yesterday_offerId
    }






if __name__ == '__main__':
    app.debug = True
    #init api port and ip address of the server
    app.run(host='localhost',port=5000)