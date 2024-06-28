from services.db import db
from flask_login import UserMixin

import uuid
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True,nullable=False, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }