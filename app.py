from flask import Flask , Response , jsonify , json ,  request
from helpers.db_helpers import run_query
import sys
from flask_cors import CORS
import bcrypt

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
    salt = bcrypt.gensalt()
    client_hash = bcrypt.hashpw(password.encode(), salt)
    if not firstName:
        return jsonify('You must input a First Name'), 400
    if firstName(firstName = int):
        return jsonify('You cannot input numbers in your name'), 400
    if not lastName:
        return jsonify('You must input a first name'), 400
    if lastName(lastName = int):
        return jsonify('You cannot input numbers in your name'), 400
    if not pictureUrl:
        return jsonify('Add one later !!'), 200
    if not username:
        return jsonify('You must input a username'), 400
    if not email:
        return jsonify('You must input an email'), 400
    if not password:
        return jsonify('You must input a password'), 400
    run_query('INSERT INTO client (firstName,lastName,pictureUrl,username,email,password) VALUES (?,?,?,?,?,?)', [firstName,lastName,pictureUrl,username,email,client_hash])
    return jsonify('User Created'), 200

# @app.patch('/api/client')
# def client_patch():
#     return

# @app.delete('/api/client')
# def client_delete():
#     return

# # CLIENT LOGIN SIDE ENDPOINTS
# @app.post('/api/client-login')
# def client_login():
#     return
# if bcrypt.checkpw(password.encode(), client_hash.encode()):
# return('You logged in')

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
    if phone_num(phone_num = str):
        return jsonify('Please input a valid phone number')
    run_query('INSERT INTO restaurant (email,name,pictureUrl,username,email,password) VALUES (?,?,?,?,?,?)', [name,address,city,email,restaurant_hash,username,bio,phone_num])
    return jsonify('Restaurant Created'), 200


# @app.patch('/api/restaurant')
# def restaurant_patch():
#     return

# # RESTAURANT LOGIN SIDE ENDPOINTS
# @app.post('/api/restaurant-login')
# def restaurant_login():
#     return
# if bcrypt.checkpw(password.encode(), restaurant_hash.encode()):
# return('You logged in')

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