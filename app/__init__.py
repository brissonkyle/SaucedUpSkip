from helpers.db_helpers import run_query
from flask import Flask, Response, request

app = Flask(__name__)

from endpoints import client_endpoints, client_log_end, restaurant_endpoints, menu_endpoints, order_endpoints, restaurant_login_end