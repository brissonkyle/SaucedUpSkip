from flask import Flask , Response , jsonify , json ,  request
from helpers.db_helpers import run_query
import sys
from flask_cors import CORS
import bcrypt
import uuid
from app import app

def grabId():
        client_id = run_query('SELECT client_id FROM client')
        return(client_id)

# CLIENT SIDE ENDPOINTS
@app.get('/api/client')
def client_get():
    client_data =  run_query('SELECT created_at, firstName, lastName, pictureUrl, username, email FROM client')
    resp = []
    for data in client_data:
        dataObj = {}
        dataObj['createdAt'] = data[0]
        dataObj['firstName'] = data[1]
        dataObj['lastName'] = data[2]
        dataObj['pictureUrl']  = data[3]
        dataObj['username'] = data[4]
        dataObj['email'] = data[5]
        dataObj['password'] = data[6]
        resp.append(dataObj)
    return jsonify(resp), 200

@app.post('/api/client')
def client_post():
    client_resp = request.json
    firstName = client_resp.get('firstName')
    lastName = client_resp.get('lastName')
    pictureUrl = client_resp.get('pictureUrl')
    username = client_resp.get('username')
    email = client_resp.get('email')
    password = client_resp.get('password')
    # salt = bcrypt.gensalt()
    # client_hash = bcrypt.hashpw(password.encode(), salt)
    if not firstName:
        return jsonify('You must input a First Name'), 400
    if not firstName.isalpha():
        return jsonify('You cannot input numbers into your name!!'), 400
    if not lastName:
        return jsonify('You must input a first name'), 400
    if not lastName.isalpha():
        return jsonify('You cannot input numbers into your name!!'), 400
    if not pictureUrl:
        return jsonify('Add one later !!'), 200
    if not username:
        return jsonify('You must input a username'), 400
    if not email:
        return jsonify('You must input an email'), 400
    if not password:
        return jsonify('You must input a password'), 400
    run_query('INSERT INTO client (firstName,lastName,pictureUrl,username,email,password) VALUES (?,?,?,?,?,?)', [firstName,lastName,pictureUrl,username,email,password])
    return jsonify('User Created'), 200

# @app.patch('/api/client')
# def client_patch():


# @app.delete('/api/client')
# def client_delete():
#     return
