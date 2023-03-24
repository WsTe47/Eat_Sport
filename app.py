import logging
from flask import Flask, request, make_response
from logconfig import *

app = Flask(__name__)


@app.route('/mes/api/v1.0/postxml', methods=['POST', 'OPTIONS', 'GET'])
def comm_postxml():
    # bl_code 和 ua_code 允许用户自行输入，用户传入 bl_code和ua_code值
    searchlists = request.get_json()
    print(searchlists)
    bl_code = searchlists['bl_code']
    ua_code = searchlists['ua_code']
    print(bl_code, ua_code)
