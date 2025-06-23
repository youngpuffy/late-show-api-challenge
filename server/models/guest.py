from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    occupation = db.Column(db.String(120), nullable=False)
    appearances = db.relationship('Appearance', backref='guest', cascade='all, delete-orphan')