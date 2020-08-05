from flask_restful import Resource
from models.owner import OwnerModel

class Owner(Resource):

    def get(self, name):
        owner = OwnerModel.find_by_name(name)
        if owner:
            return owner.json()
        return {'message': 'Owner not found'}, 404

    def post(self, name):
        if OwnerModel.find_by_name(name):
            return {'message': "A owner with name '{}' already exists.".format(name)}, 400

        owner = OwnerModel(name)

        try:
            owner.save_to_db()
        except:
            return {"message": "An error occurred creating the owner."}, 500

        return owner.json(), 201

    def delete(self, name):
        owner = OwnerModel.find_by_name(name)
        if owner:
            owner.delete_from_db()

        return {'message': 'Owner deleted'}


class OwnersList(Resource):
    def get(self):
        return {'owners': list(map(lambda x: x.json(), OwnerModel.query.all()))}
