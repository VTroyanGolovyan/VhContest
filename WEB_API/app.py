from flask import Flask
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'  # Allow cros domain
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@server:3306/VHcontest'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from db_models import *


@app.route('/')
def home():
    return 'Home route'


@app.route('/sign/in', methods=['POST', 'OPTIONS'])
def sign_in():
    return json.dumps({
        'status': '0',
        'token': 'HIUGHIUHUHUIUHUIHS',
        'refresh_token': 'HIUHUUIHUIHU'
    })


@app.route('/sign/up')
def sign_up():
    return 'Sign up route!'


@app.route('/sign/out')
def sign_out():
    return 'Sign out route!'


@app.route('/task_list')
def archive():
    return json.dumps({
        'status': '0',
        'data': [
            {
                'id': i,
                'name': 'Hello, world',
                'condition': 'Напишите Hello, world',
                'timeLimit': '1000',
                'memoryLimit': '128'
            } for i in range(1, 15)
        ]
    })


@app.route('/task')
def task():
    return 'Hello World!'


@app.route('/check')
def check():
    return 'Task check!'


if __name__ == '__main__':
    app.run()
