from app import db
import json


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    last_name = db.Column(db.String(100), unique=False, nullable=False)
    patronymic = db.Column(db.String(100), unique=False, nullable=False)
    email = db.Column(db.String(200), unique=False, nullable=False)
    password = db.Column(db.String(300), unique=False, nullable=False)
    salt = db.Column(db.String(10), unique=False, nullable=False)

    def __repr__(self):
        return 'ih'


class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), unique=False)
    condition = db.Column(db.Text, unique=False)
    time_limit = db.Column(db.Integer, unique=False)
    memory_limit = db.Column(db.Integer, unique=False)
    process_limit = db.Column(db.Integer, unique=False)
    test_generator = db.Column(db.Text, unique=False)
    test_generator_language = db.Column(db.String(20), unique=False)
    checker = db.Column(db.Text, unique=False)
    checker_language = db.Column(db.String(20), unique=False)
    author_solution = db.Column(db.Text, unique=False)
    author_solution_language = db.Column(db.String(20), unique=False)

    def __repr__(self):
        res = {
            'id': self.id,
            'condition': self.condition,
            'time_limit': self.time_limit,
            'memory_limit': self.memory_limit
        }
        return json.dumps(res)

    def __str__(self):
        res = {
            'id': self.id,
            'name': self.name,
            'condition': self.condition,
            'time_limit': self.time_limit,
            'memory_limit': self.memory_limit
        }
        return json.dumps(res)


class Test(db.Model):
    __tablename__ = 'tests'
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, unique=False, nullable=False)
    input = db.Column(db.Text, unique=False)
    output = db.Column(db.Text, unique=False)

    def __repr__(self):
        pass


class TestResult(db.Model):
    __tablename__ = 'tests_results'
    id = db.Column(db.Integer, primary_key=True)
    sending_id = db.Column(db.Integer, unique=False)
    test_id = db.Column(db.Integer, unique=False)
    output = db.Column(db.String(20), unique=False)

    def __repr__(self):
        pass


class Sending(db.Model):
    __tablename__ = 'sendings'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer, unique=False)
    user_id = db.Column(db.Integer, unique=False)
    task_id = db.Column(db.Integer, unique=False)
    code = db.Column(db.Text, unique=False)
    language = db.Column(db.String(100), unique=False)
    result = db.Column(db.String(20), unique=False)
    time = db.Column(db.Integer, unique=False)
    memory = db.Column(db.Integer, unique=False)

    def __repr__(self):
        res = {
            'id': self.id,
            'task_id': self.task_id,
            'user_id': self.user_id,
            'result': self.result,
            'time': self.time,
            'memory': self.memory
        }
        return json.dumps(res)

    def __str__(self):
        res = {
            'id': self.id,
            'task_id': self.task_id,
            'user_id': self.user_id,
            'result': self.result,
            'time': self.time,
            'memory': self.memory
        }
        return json.dumps(res)
