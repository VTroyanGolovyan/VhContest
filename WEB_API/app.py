from flask import Flask, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from check_solution_adapter import CheckAdapter

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'  # Allow cros domain
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/VHcontest'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from db_models import *


@app.route('/')
def home():
    return 'Home route'


@app.route('/sign/in', methods=['POST', 'OPTIONS'])
def sign_in():
    if request.method == 'POST':
        print(request.data)
        return json.dumps({
            'status': '0',
            'token': 'HIUGHIUHUHUIUHUIHS',
            'refresh_token': 'HIUHUUIHUIHU'
        })
    else:
        return ''


@app.route('/sign/up')
def sign_up():
    return 'Sign up route!'


@app.route('/sign/out')
def sign_out():
    return 'Sign out route!'


@app.route('/task_list')
def archive():
    tasks = Task.query.all()
    for task in tasks:
        print(str(task))
    return json.dumps({
        'status': '0',
        'data': [json.loads(str(t)) for t in tasks]
    })


@app.route('/task/<id>', methods=['GET', 'OPTIONS'])
def task(id):
    task = Task.query.get(id)
    print(task)
    return json.dumps({
        'status': '0',
        'data': json.loads(str(task))
    })


@app.route('/check', methods=['POST', 'OPTIONS'])
def check():
    if request.method == 'POST':
        data = json.loads(request.data)
        sending = Sending(
            type=1,
            user_id=1,
            task_id=1,
            code=data['solution'],
            language='python',
            result='P'
        )
        db.session.add(sending)
        db.session.commit()
        check = CheckAdapter('localhost', 6666)
        print(check.say_server(1, sending.id))
        return 'Task check!'
    else:
        return ''


if __name__ == '__main__':
    app.run()
