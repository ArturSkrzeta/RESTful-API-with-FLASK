from db import db
# from app import db

class OwnerModel(db.Model):

    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key=True)    # will be created automatically once db session commit and can be accessed form python object level
    name = db.Column(db.String(80))
    items = db.relationship('ItemModel')

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
