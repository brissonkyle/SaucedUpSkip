from app import app
from flask import Flask , Response , jsonify , json ,  request
from helpers.db_helpers import run_query
import sys
from flask_cors import CORS


# MENU ENDPOINTS
@app.get('/api/menu')
def menu_get():
    menu_data = run_query('SELECT name,description,price,imageUrl,id,restaurant_id FROM menu_item')
    resp = []
    for data in menu_data:
        dataObj = {}
        dataObj['name'] = data[0]
        dataObj['description'] = data[1]
        dataObj['price'] = data[2]
        dataObj['imageUrl'] = data[3]
        dataObj['restaurant_id'] = data[4]
        dataObj['id'] = data[5]
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
    restaurant_token = menu_resp.get('restaurant_token')
    if restaurant_token:
        run_query('INSERT INTO menu_item (restaurant_id,restaurant_token,name,description,price,imageUrl) VALUES (?,?,?,?,?,?)', [restaurant_id,restaurant_token,name,description,price,imageUrl])
        return jsonify('Item Created'), 201
    if not restaurant_token:
        return jsonify('Must provide a valid session token'), 401


@app.patch('/api/menu')
def menu_patch():
    menu_resp = request.json
    token = menu_resp.get('token')
    name = menu_resp.get('name')
    description = menu_resp.get('description')
    price = menu_resp.get('price')
    imageUrl = menu_resp.get('imageUrl')
    id = menu_resp.get('id')
    if token:
        run_query('UPDATE menu_item SET name=?,description=?,price=?,imageUrl=? WHERE id=?', [name,description,price,imageUrl,id])
        return jsonify('Item Updated'), 201
    if not token:
        return jsonify('Must provide a valid session token'), 401

@app.delete('/api/menu')
def menu_delete():
    menu_resp = request.json
    restaurant_token = menu_resp.get('restaurant_token')
    if restaurant_token:
        run_query('DELETE FROM menu_item WHERE restaurant_token=?', [restaurant_token])
        return jsonify('Menu item deleted'), 201
    if restaurant_token:
        return jsonify('Must provide a valid menu id and token'), 401