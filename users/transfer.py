from flask import Blueprint
from flask_restx import Api,Resource

bp = Blueprint('transfer',__name__)
api = Api(bp)

transfer_model = api.parser()
transfer_model.add_argument('user_from_id',type = int,required = True)
transfer_model.add_argument('user_from_card',type = int,required = True)
transfer_model.add_argument('to_card',type = int,required = True)
transfer_model.add_argument('amount',type = float,required = True)


@api.route('/transfer-money')
class TransferMoney(Resource):
    @api.expect(transfer_model)
    def post(self):
        return ''