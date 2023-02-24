from flask_restx import Api,Resource
from database.models import User,Card,Payment
from business import api


invoice_model = api.parser()
invoice_model.add_argument('service_id',type=int,required = True)
invoice_model.add_argument('service_name',type=str,required = True)
invoice_model.add_argument('amount',type=float,required = True)
invoice_model.add_argument('phone_number',type=str,required = True)


@api.route('/send-invoice')
class SendInvoice(Resource):
    @api.expect(invoice_model)
    def post(self):
        args = invoice_model.parse_args()

        service_id = args.get('service_id')
        service_name = args.get('service_name')
        amount = args.get('amount')
        phone_number = args.get('phone_number')

        user_id = User.query.filter_by(user_phone_number=phone_number).first().id
        card_number = Card.query.filter_by(user_id=user_id).first().card_number
        payment = Payment().register_pay(card_number,amount,service_name)

        if payment:
            return {'status':1,'message':'Успешно'}
        else:
            return {'status':0,'message':'Недостаточно средств'}
