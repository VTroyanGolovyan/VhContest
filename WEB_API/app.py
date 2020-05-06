from flask import Flask, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from check_solution_adapter import CheckAdapter
import tokenizer

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
        form_data = json.loads(request.data.decode('utf-8'))
        user = db.session.query(User).filter_by(email=form_data['email']).all()
        if len(user) != 0:
            user_data = json.loads(str(user[0]))
            pass_hash = tokenizer.get_hash(form_data['password'], user_data['salt'])
            if pass_hash != user_data['password']:
                return json.dumps({
                    'status': '2',
                    'token': '',
                    'refresh_token': ''
                })
            else:
                token = tokenizer.generate_token(100)
                refresh_token = tokenizer.generate_token(100)
                print(token)
                db.session.add(Session(
                    user=user_data['id'],
                    token=token,
                    refresh_token=refresh_token
                ))
                db.session.commit()
                return json.dumps({
                    'status': '0',
                    'token': token,
                    'refresh_token': refresh_token
                })
        else:
            return json.dumps({
                'status': '1',
                'token': '',
                'refresh_token': ''
            })
    else:
        return ''


@app.route('/sign/up')
def sign_up():
    return ''


@app.route('/<token>/sign/out')
def sign_out(token):
    user = tokenizer.get_user(db, token)
    if user:
        session = db.session.query(Session).filter_by(token=token).first()
        db.session.delete(session)
        db.session.commit()
    return ''


@app.route('/<token>/task_list', methods=['GET', 'OPTIONS'])
def task_list(token):
    user = tokenizer.get_user(db, token)
    if user:
        tokenizer.get_user(db, token)
        tasks = db.session.query(Task).all()
        return json.dumps({
            'status': '0',
            'data': [json.loads(str(t)) for t in tasks]
        })
    else:
        return json.dumps({
            'status': '403',
            'data': ''
        })


@app.route('/<token>/task/<id>', methods=['GET', 'OPTIONS'])
def task(token, id):
    user = tokenizer.get_user(db, token)
    if user:
        task = db.session.query(Task).get(id)
        return json.dumps({
            'status': '0',
            'data': json.loads(str(task))
        })
    else:
        return json.dumps({
            'status': '403',
            'data': ''
        })


@app.route('/<token>/check', methods=['POST', 'OPTIONS'])
def check(token):
    user = tokenizer.get_user(db, token)
    if user:
        if request.method == 'POST':
            data = json.loads(request.data)
            print(data)
            sending = Sending(
                type=1,
                user_id=user,
                task_id=data['task_id'],
                code=data['solution'],
                language=data['language'],
                result='P',
                time=0,
                memory=0
            )
            db.session.add(sending)
            db.session.commit()
            # send info to testing server
            check = CheckAdapter('localhost', 65500)
            check.say_server(1, sending.id)
            return json.dumps({
                'status': '0',
            })
    return json.dumps({
        'status': '403',
    })


@app.route('/<token>/attempts/<task_id>', methods=['GET', 'OPTIONS'])
def attempts(token, task_id):
    user = tokenizer.get_user(db, token)
    if user:
        attempts = db.session.query(Sending).filter_by(task_id=task_id).all()
        db.session.close()
        return json.dumps({
            'status': '0',
            'data': [json.loads(str(attempt)) for attempt in attempts]
        })
    else:
        return json.dumps({
            'status': '403',
            'data': ''
        })


if __name__ == '__main__':
    app.run()
