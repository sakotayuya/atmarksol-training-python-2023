from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    status = db.Column(db.Enum('enable', 'disable'))
    deleted = db.Column(db.Boolean)