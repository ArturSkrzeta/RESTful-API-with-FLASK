from flask_restful import Resource
from models.payer import PayerModel

class Payer(Resource):

    def get(self, name):
        payer = PayerModel.find_by_name(name)
        if payer:
            return payer.json()
        return {'message': 'Payer not found'}, 404

    def post(self, name):
        if PayerModel.find_by_name(name):
            return {'message': "A payer with name '{}' already exists.".format(name)}, 400

        payer = PayerModel(name)

        try:
            payer.save_to_db()
        except:
            return {"message": "An error occurred creating the payer."}, 500

        return payer.json(), 201

    def delete(self, name):
        payer = PayerModel.find_by_name(name)
        if payer:
            payer.delete_from_db()

        return {'message': 'Payer deleted'}


class PayersList(Resource):
    def get(self):
        return {'payers': list(map(lambda x: x.json(), PayerModel.query.all()))}
