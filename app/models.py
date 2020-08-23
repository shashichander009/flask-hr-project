from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login, db


@login.user_loader
def load_user(id):
    return Admin.query.get(int(id))


class Admin(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Email {}>'.format(self.email)


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    phone = db.Column(db.String(120), nullable=False, unique=True)
    location = db.Column(db.String(120), nullable=False,)
    salary = db.Column(db.BIGINT, nullable=False)

    def __repr__(self):
        return '<Employees {}>'.format(self.email)
