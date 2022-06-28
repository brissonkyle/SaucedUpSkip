from app import app
from flask import Flask , Response , jsonify , json ,  request
from helpers.db_helpers import run_query
import sys
from flask_cors import CORS


# ORDER ENDPOINTS 
@app.get('/api/order')
def order_get():
    order_data = run_query('SELECT name,description,price,imageUrl FROM menu_item')
    resp = []
    for data in order_data:
        dataObj = {}
        dataObj['name'] = data[0]
        dataObj['description'] = data[1]
        dataObj['price'] = data[2]
        dataObj['imageUrl'] = data[3]
        resp.append(dataObj)
    return jsonify(resp), 200

# @app.post('/api/order')
# def order_post():
#     return

# @app.patch('/api/order')
# def order_patch():
#     return