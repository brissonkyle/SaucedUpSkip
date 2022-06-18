from app import app
from flask import Flask , Response , jsonify , json ,  request
from helpers.db_helpers import run_query
import sys
from flask_cors import CORS


# # MENU ENDPOINTS
# @app.get('/api/menu')
# def menu_get():
#     return

# @app.post('/api/menu')
# def menu_post():
#     menu_resp = request.json
#     name = menu_resp.get('name')
#     description = menu_resp.get('description')
#     price = menu_resp.get('price')
#     if not name:
#         return('Your item Must have a name')


# @app.patch('/api/menu')
# def menu_patch():
#     return

# @app.delete('/api/menu')
# def menu_delete():
#     return