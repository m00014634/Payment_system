
from flask_restx import Resource,Api
from database.models import Card
from users import api

card_model = api.parser()
card_model.add_argument('card_number',type = str,required = True)
card_model.add_argument('user_id',type = int,required = True)
card_model.add_argument('amount',type = float,required = True)
card_model.add_argument('exp_date',type = str ,required = False)
card_model.add_argument('phone_number',type = str ,required = False)


@api.route('/add-card')
class AddCart(Resource):
    @api.expect(card_model)
    def post(self):
        response = card_model.parse_args()

        card_number = response.get('card_number')
        user_id = response.get('user_id')
        amount = response.get('amount')
        exp_date = response.get('exp_date')
        phone_number = response.get('phone_number')



        new_card = Card().register_card(card_number,user_id,amount,exp_date,phone_number)
        return {'status':1,'message': new_card}



