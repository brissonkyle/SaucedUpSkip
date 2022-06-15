from flask import Flask , Response , jsonify , json ,  request
from helpers.db_helpers import run_query
import sys
from flask_cors import CORS


app = Flask(__name__)

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
        resp.append(dataObj)
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

# RESTAURANT SIDE ENDPOINTS
@app.get('/api/restaurant')
def restaurant_get():
    restaurant_data =  run_query('SELECT email, name, address, city, bio, phone_num, banner_url, profileUrl FROM restaurant')
    resp = []
    for data in restaurant_data:
        dataObj = {}
        dataObj['email'] = data[0]
        dataObj['name'] = data[1]
        dataObj['address'] = data[2]
        dataObj['city']  = data[3]
        dataObj['username'] = data[4]
        dataObj['bio'] = data[5]
        dataObj['phone_num'] = data[6]
        dataObj['banner_url'] = data[7]
        dataObj['profileUrl'] = data[8]
        resp.append(dataObj)
    return jsonify(resp), 200

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

if len(sys.argv) > 1:
    mode = sys.argv[1]
else:
    print('Missing required arguments')
    exit

if mode == 'testing':
    from flask_cors import CORS
    CORS(app)
    app.run(debug=True)
elif mode == 'production':
    import bjoern
    bjoern.run(app, '0.0.0.0', 5005)
else :
    print('Mode must be in testing/production')
    exit()