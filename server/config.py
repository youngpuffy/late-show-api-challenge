import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'salite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'super-secret')