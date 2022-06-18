from flask import Flask , Response , jsonify , json ,  request
from helpers.db_helpers import run_query
import sys
from flask_cors import CORS
import bcrypt
import uuid
from app import app

# RESTAURANT SIDE ENDPOINTS
@app.get('/api/restaurant')
def restaurant_get():
    restaurant_data =  run_query('SELECT email, name, address, city, bio, phone_num, banner_url, profileUrl FROM restaurant')
    resp = []
    for data in restaurant_data:
        dataObj = {}
        dataObj['email'] = data[0]
        dataObj['password'] = data[1]
        dataObj['name'] = data[2]
        dataObj['address'] = data[3]
        dataObj['city']  = data[4]
        dataObj['username'] = data[5]
        dataObj['bio'] = data[6]
        dataObj['phone_num'] = data[7]
        # dataObj['banner_url'] = data[7]
        # dataObj['profileUrl'] = data[8]
        resp.append(dataObj)
    return jsonify(resp), 200

@app.post('/api/restaurant')
def restaurant_post():
    restaurant_resp = request.json
    email = restaurant_resp.get('email')
    password = restaurant_resp.get('password')
    salt = bcrypt.gensalt()
    restaurant_hash = bcrypt.hashpw(password.encode(), salt)
    name = restaurant_resp.get('name')
    address = restaurant_resp.get('address')
    city = restaurant_resp.get('city')
    username = restaurant_resp.get('username')
    bio = restaurant_resp.get('bio')
    phone_num = restaurant_resp.get('phone_num')
    if not email:
        return jsonify('You must input an email'), 400
    if not password:
        return jsonify('You mus input a password')
    if not name:
        return jsonify('You must input a restaurant name'), 400
    if not address:
        return jsonify('Add one later !!'), 200
    if not city:
        return jsonify('You must input a city'), 400
    if not username:
        return jsonify('You must input a username'), 400
    if not bio:
        return jsonify('You must add a bio')
    if not phone_num:
        return jsonify('You must add a phone number')
    if not phone_num.isnumeric():
        return jsonify('Please input a valid phone number')
    run_query('INSERT INTO restaurant (email,name,pictureUrl,username,email,password) VALUES (?,?,?,?,?,?)', [name,address,city,email,restaurant_hash,username,bio,phone_num])
    return jsonify('Restaurant Created'), 200


# @app.patch('/api/restaurant')
# def restaurant_patch():
#     return
