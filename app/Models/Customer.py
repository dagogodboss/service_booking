from app import db
from datetime import datetime


class Customer(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    email = db.Column(db.String(1024), nullable=False)
    name = db.Column(db.String(1024), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, default=datetime.utcnow)
    workorders = db.relationship('WorkOrder')

    def __repr__(self):
        return '<Customer {}>'.format(self.name)