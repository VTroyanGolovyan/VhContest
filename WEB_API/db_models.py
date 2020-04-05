from app import db


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
        pass


class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        pass


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
    sending_id = db.Column(db.Integer, unique=False)
    test_id = db.Column(db.Integer, unique=False)
    output = db.Column(db.String(20), unique=False)

    def __repr__(self):
        pass
