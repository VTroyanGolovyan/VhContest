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
        return '<User %r>' % self.name
