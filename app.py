import mariadb
from flask import Flask , Response , jsonify , json ,  request
from helpers.db_helpers import run_query

app = Flask(__name__)

# CLIENT SIDE ENDPOINTS
@app.get('/api/client')
def client_get():
    resp =  request.args
    email = request.args.get('email')
    firstName = request.args.get('firstName')
    lastName = request.args.get('lastName')
    username = request.args.get('username')
    createdAt = request.args.get('created_at')
    pictureUrl = request.args.get('pictureUrl')
    run_query('SELECT ?, ?, ?, ?, ?, ? FROM client', [email,firstName,lastName,username,createdAt,pictureUrl])
    return jsonify(resp), 200

# @app.post('/api/client')
# def client_post():
#     return

# @app.patch('/api/client')
# def client_patch():
#     return

# @app.delete('/api/client')
# def client_delete():
#     return

# # CLIENT LOGIN SIDE ENDPOINTS
# @app.post('/api/client-login')
# def client_post():
#     return

# @app.delete('/api/client-login')
# def client_delete():
#     return

# # RESTAURANT SIDE ENDPOINTS
# @app.get('/api/restaurant')
# def restaurant_get():
#     return

# @app.post('/api/restaurant')
# def restaurant_post():
#     return

# @app.patch('/api/restaurant')
# def restaurant_patch():
#     return

# # RESTAURANT LOGIN SIDE ENDPOINTS
# @app.post('/api/restaurant-login')
# def restaurant_post():
#     return

# @app.delete('/api/restaurant-login')
# def restaurant_delete():
#     return

# # MENU ENDPOINTS
# @app.get('/api/menu')
# def menu_get():
#     return

# @app.post('/api/menu')
# def menu_post():
#     return

# @app.patch('/api/menu')
# def menu_patch():
#     return

# @app.delete('/api/menu')
# def menu_delete():
#     return

# # ORDER ENDPOINTS 
# @app.get('/api/menu')
# def order_get():
#     return

# @app.post('/api/menu')
# def order_post():
#     return

# @app.patch('/api/menu')
# def order_patch():
#     return