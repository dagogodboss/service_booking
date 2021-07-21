from app import db
from datetime import datetime


class WorkOrder(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    service_id = db.Column(db.Integer,
                           db.ForeignKey('services.id'),
                           nullable=False)
    customer_id = db.Column(db.Integer,
                            db.ForeignKey('customer.id'),
                            nullable=False)
    employee_id = db.Column(db.Integer,
                            db.ForeignKey('customer.id'),
                            nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<WorkOrder {}>'.format(self.name)
