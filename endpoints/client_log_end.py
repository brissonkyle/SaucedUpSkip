from app import app
from flask import Flask , Response , jsonify , json ,  request
from helpers.db_helpers import run_query
import sys
from flask_cors import CORS
import uuid

# CLIENT LOGIN SIDE ENDPOINTS
@app.post('/api/client-login')
def client_login():
    client_resp = request.json
    token = uuid.uuid4().hex
    client_id = client_resp.get('client_id')
    run_query('INSERT INTO client_session (token,client_id) VALUES (?,?)', [token,client_id])
    return(client_resp), 200

# @app.delete('/api/client-login')
# def client_delete():
#     return