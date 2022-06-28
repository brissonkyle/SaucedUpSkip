from app import app
from flask import Flask , Response , jsonify , json ,  request
from helpers.db_helpers import run_query
import sys
from flask_cors import CORS


# MENU ENDPOINTS
@app.get('/api/menu')
def menu_get():
    menu_data = run_query('SELECT name,description,price,imageUrl FROM menu_item')
    resp = []
    for data in menu_data:
        dataObj = {}
        dataObj['name'] = data[0]
        dataObj['description'] = data[1]
        dataObj['price'] = data[2]
        dataObj['imageUrl'] = data[3]
        resp.append(dataObj)
    return jsonify(resp), 200

@app.post('/api/menu')
def menu_post():
    menu_resp = request.json
    restaurant_id = menu_resp.get('restaurant_id')
    name = menu_resp.get('name')
    description = menu_resp.get('description')
    price = menu_resp.get('price')
    imageUrl = menu_resp.get('imageUrl')
    token = run_query('SELECT token FROM restaurant_session WHERE restaurant_id=?', [restaurant_id])
    if token:
        run_query('INSERT INTO menu_item (restaurant_id,name,description,price,imageUrl) VALUES (?,?,?,?,?)', [restaurant_id,name,description,price,imageUrl])
        return jsonify('Item Created'), 201
    if not token:
        return jsonify('Must provide a valid session token'), 401


# @app.patch('/api/menu')
# def menu_patch():
#     result = run_query('SELECT name,description,price,imageUrl FROM restaurant_session')
#     name = result.get('name')
#     description = result.get('description')
#     price = result.get('price')
#     imageUrl = result.get('imageUrl')

# @app.delete('/api/menu')
# def menu_delete():
#     pass 