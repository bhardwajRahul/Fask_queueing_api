from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis

db = SQLAlchemy()
redis_cache = FlaskRedis()

class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50))
    platform = db.Column(db.String(20))

    def __init__(self, user_id, platform):
        self.user_id = user_id
        self.platform = platform
