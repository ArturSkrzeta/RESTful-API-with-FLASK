from flask_restful import Resource, reqparse
from models.transaction import TransactionModel
from datetime import datetime

class Transaction(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('amount',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    parser.add_argument('payer_id',
                        type=int,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    parser.add_argument('currency',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    parser.add_argument('time',
                        type=lambda x: datetime.strptime(x,'%Y-%m-%d %H:%M:%S'),
                        # type=str,
                        required=True,
                        # help="This field cannot be left blank!"
                        )


    def get(self, transaction_id):
        transaction = TransactionModel.find_by_transaction_id(transaction_id)
        if transaction:
            return transaction.json()
        return {'message': 'Transaction not found'}, 404

    def post(self, transaction_id):
        if TransactionModel.find_by_transaction_id(transaction_id):
            return {'message': "An transaction with transaction_id '{}' already exists.".format(transaction_id)}, 400

        data = Transaction.parser.parse_args()
        transaction = TransactionModel(transaction_id, **data)

        try:
            transaction.save_to_db()
        except:
            return {"message": "An error occurred inserting the transaction."}, 500

        return transaction.json(), 201

    def delete(self, transaction_id):
        transaction = TransactionModel.find_by_transaction_id(transaction_id)
        if transaction:
            transaction.delete_from_db()
            return {'message': 'Transaction deleted.'}
        return {'message': 'Transaction not found.'}, 404

    def put(self, transaction_id):
        data = Transaction.parser.parse_args()

        transaction = TransactionModel.find_by_transaction_id(transaction_id)

        if transaction:
            transaction.price = data['price']
            transaction.payer_id = data['payer_id']
        else:
            transaction = TransactionModel(transaction_id, **data)

        transaction.save_to_db()

        return transaction.json()
