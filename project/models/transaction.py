from db import db
from datetime import datetime
# from app import db

class TransactionModel(db.Model):

    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    transaction_id = db.Column(db.String(80))
    amount = db.Column(db.Float(precision=2))
    currency =  db.Column(db.String(3))
    time = db.Column(db.DateTime)
    # time = db.Column(db.String(20))

    # to delete owner I need to delete items where the owner is assigned to
    payer_id = db.Column(db.Integer, db.ForeignKey('payers.id')) # this is a consecutive id integer from primary_key owners table
    payer = db.relationship('PayerModel')

    def __init__(self, transaction_id, amount, currency, time, payer_id):
        self.transaction_id = transaction_id
        self.amount = amount
        self.currency = currency
        self.time = time
        self.payer_id = payer_id

    def json(self):
        return {'transaction_id': self.transaction_id, 'payer': self.payer_id, 'price': self.amount, 'currency': self.currency, 'time': str(self.time)}

    @classmethod
    def find_by_transaction_id(cls, transaction_id):
        return cls.query.filter_by(transaction_id=transaction_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
