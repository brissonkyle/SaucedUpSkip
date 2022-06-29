from app import app
from flask import Flask , Response , jsonify , json ,  request
from helpers.db_helpers import run_query
import sys
from flask_cors import CORS


# ORDER ENDPOINTS 
# @app.get('/api/order')
# def order_get():
#     order_data = run_query('SELECT name,description,price,imageUrl FROM menu_item')
#     resp = []
#     for data in order_data:
#         dataObj = {}
#         resp.append(dataObj)
#     return jsonify(resp), 200

@app.post('/api/order')
def order_post():
    order_resp = request.json
    rest_id = order_resp.get('restaurant_id')
    id = order_resp.get('id')
    client_id = run_query('SELECT id FROM client WHERE id=?', [id])
    restaurant_id = run_query('SELECT id FROM restaurant WHERE id=?', [rest_id])

# @app.patch('/api/order')
# def order_patch():
#     return