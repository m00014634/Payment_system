from flask import Blueprint
from flask_restx import Api,Resource

bp = Blueprint('payment',__name__)
api = Api(bp)

payment_model = api.parser()
payment_model.add_argument('service_id',type = int, required = True)
payment_model.add_argument('amount',type = float, required = True)
payment_model.add_argument('from_card',type = int , required = True)

@api.route('/pay-service')
class PayService(Resource):
    @api.expect(payment_model)
    def post(self):
        return ''