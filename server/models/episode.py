from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(80),nullable=False)
    number = db.column(db.Integer, nullable=False)
    appearances = db.relationship('Appearance', backref='guest', cascade='all, delete-orphan')