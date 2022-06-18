from app import app
from flask import Flask , Response , jsonify , json ,  request
from helpers.db_helpers import run_query
import sys
from flask_cors import CORS


# # RESTAURANT LOGIN SIDE ENDPOINTS
# @app.post('/api/restaurant-login')
# def restaurant_login():
#     return
# if bcrypt.checkpw(password.encode(), restaurant_hash.encode()):
# return('You logged in')

# @app.delete('/api/restaurant-login')
# def restaurant_delete():
#     return