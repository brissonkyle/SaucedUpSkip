from app import app
from flask import Flask , Response , jsonify , json ,  request
from helpers.db_helpers import run_query
from flask_cors import CORS
import uuid


# FUNCTION FOR GRABBING ID
def grabId(email,password):
    result = run_query('SELECT id FROM client WHERE email=? AND password=?',[email,password])
    if result == []:
        return None
    client_id = result[0][0]
    return client_id

# CLIENT LOGIN SIDE ENDPOINTS
@app.post('/api/client-login')
def client_login():
    client_resp = request.json
    email = client_resp.get('email')
    password = client_resp.get('password')
    token = uuid.uuid4().hex
    client_id = grabId(email,password)
    if client_id == None:
        return('Invalid Email and Password'), 401
    run_query('INSERT INTO client_session (token,client_id) VALUES (?,?)', [token,client_id])
    return jsonify(token,client_id), 201

@app.delete('/api/client-login')
def client_logout():
    client_resp = request.json
    token = client_resp.get('token')
    if token:
        run_query('DELETE FROM client_session WHERE token=?', [token])
        return jsonify('You logged out'), 204
    if not token:
        return jsonify('Must provide a valid session token'), 401