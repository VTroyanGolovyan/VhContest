from flask import Flask
import json


app = Flask(__name__)


@app.route('/')
def main():
    return 'Home route'


@app.route('/sign/in')
def sign_in():
    return 'Sign in route!'


@app.route('/sign/up')
def sign_up():
    return 'Sign up route!'


@app.route('/sign/out')
def sign_out():
    return 'Sign out route!'


@app.route('/archive')
def archive():
    return 'Tasks archive route'


@app.route('/task')
def task():
    return 'Hello World!'


@app.route('/check')
def task():
    return 'Task check!'


if __name__ == '__main__':
    app.run()

