from flask import Flask, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from check_solution_adapter import CheckAdapter

app = Flask(__name__)
# Allow cross domain
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)
db_url = 'mysql://root:root@localhost:3306/VHcontest'
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from db_models import *


@app.route('/')
def home():
    return json.dumps({
            'status': '0'
    })


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
    return ''


@app.route('/sign/out')
def sign_out():
    return ''


@app.route('/task_list', methods=['GET', 'OPTIONS'])
def task_list():
    tasks = db.session.query(Task).all()
    for task in tasks:
        print(str(task))
    return json.dumps({
        'status': '0',
        'data': [json.loads(str(t)) for t in tasks]
    })


@app.route('/task/<id>', methods=['GET', 'OPTIONS'])
def task(id):
    task = db.session.query(Task).get(id)
    return json.dumps({
        'status': '0',
        'data': json.loads(str(task))
    })


@app.route('/check', methods=['POST', 'OPTIONS'])
def check():
    if request.method == 'POST':
        data = json.loads(request.data)
        print(data['task_id'])
        sending = Sending(
            type=1,
            user_id=1,
            task_id=data['task_id'],
            code=data['solution'],
            language='python',
            result='P',
            time=0,
            memory=0
        )
        db.session.add(sending)
        db.session.commit()
        # send info to testing server
        check = CheckAdapter('localhost', 6666)
        check.say_server(1, sending.id)
        return ''
    else:
        return ''


@app.route('/attempts/<id>', methods=['GET', 'OPTIONS'])
def attempts(id):
    attempts = db.session.query(Sending).filter_by(task_id=id).all()
    db.session.close()
    return json.dumps({
        'status': '0',
        'data': [json.loads(str(attempt)) for attempt in attempts]
    })


if __name__ == '__main__':
    app.run()
