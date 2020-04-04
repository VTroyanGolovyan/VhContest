from flask import Flask
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)


@app.route('/')
@cross_origin()
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
                'id': '1',
                'name': 'Hello, world',
                'condition': 'Напишите Hello, world',
                'timeLimit': '1000',
                'memoryLimit': '128'
            }
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
