from app import db
from datetime import datetime


class Service(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250), nullable=True)
    duration = db.Column(db.String(250), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, default=datetime.utcnow)
    workorders = db.relationship('WorkOrder')

    def __repr__(self):
        return '<Service {}>'.format(self.name)
