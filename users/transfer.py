from flask_restx import Api,Resource
from database.models import TransfersP2P
from users import api
import random

transfer_model = api.parser()
transfer_model.add_argument('user_from_id',type = int,required = True)
transfer_model.add_argument('user_from_card',type = int,required = True)
transfer_model.add_argument('to_card',type = int,required = True)
transfer_model.add_argument('amount',type = float,required = True)
transfer_model.add_argument('verify_code',type = str,required = True)

model_verify = api.parser()
model_verify.add_argument('card_number',type = str, required = True)
test_ver = {}

@api.route('/transfer-money')
class TransferMoney(Resource):
    @api.expect(transfer_model)
    def post(self):
        args  = transfer_model.parse_args()

        user_from_id = args.get('user_from_id')
        user_from_card =args.get('user_from_card')
        to_card = args.get('to_card')
        amount = args.get('amount')
        code = args.get('verify_code')

        if test_ver[user_from_card] == code:
            result = TransfersP2P().register_pay(user_from_id,user_from_card,to_card,amount)

            return {'status':1,'message':result}
        return {'status':0,'message': 'За тобой уже выехали'}



# Pay for some service

@api.route('/get-verify-code')
class GetVerify(Resource):
    @api.expect(model_verify)
    def get(self):
        args = model_verify.parse_args()
        card_number = args.get('card_number')
        verify_code = random.randint(1212,9999)

        test_ver[card_number] = verify_code

        return {'status':1,'code':verify_code}