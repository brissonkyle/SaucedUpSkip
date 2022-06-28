from urllib import response
import uuid
from app import app
from flask import Flask , Response , jsonify , json ,  request
from helpers.db_helpers import run_query
import sys
from flask_cors import CORS

# FUNCTION FOR GRABBING ID
def grabId(email,password):
    result = run_query('SELECT id FROM restaurant WHERE email=? AND password=?',[email,password])
    if result == []:
        return None
    restaurant_id = result[0][0]
    return restaurant_id

# RESTAURANT LOGIN SIDE ENDPOINTS
@app.post('/api/restaurant-login')
def restaurant_login():
    restaurant_resp = request.json
    email = restaurant_resp.get('email')
    password = restaurant_resp.get('password')
    token = uuid.uuid4().hex
    restaurant_id = grabId(email,password)
    run_query('INSERT INTO restaurant_session (restaurant_token,restaurant_id) VALUES (?,?)', [token,restaurant_id])
    return jsonify(token,restaurant_id), 201

@app.delete('/api/restaurant-login')
def restaurant_logout():
    restaurant_resp = request.json
    restaurant_token = restaurant_resp.get('restaurant_token')
    if restaurant_token:
        run_query('DELETE FROM restaurant_session WHERE restaurant_token=?', [restaurant_token])
        return jsonify('You logged out'), 204
    if not restaurant_token:
        return jsonify('Must provide a valid session token'), 401


# if bcrypt.checkpw(password.encode(), restaurant_hash.encode(), salt):
# return('You logged in')