from flask import Blueprint
from flask_restx import Api,Resource


bp = Blueprint('invoice',__name__)
api = Api(bp)


invoice_model = api.parser()
invoice_model.add_argument('service_id',type=int,required = True)
invoice_model.add_argument('service_name',type=str,required = True)
invoice_model.add_argument('amount',type=float,required = True)
invoice_model.add_argument('phone_number',type=str,required = True)


@api.route('/send-invoice')
class SendInvoice(Resource):
    @api.expect(invoice_model)
    def post(self):
        pass
