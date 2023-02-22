from datetime import datetime
from flask import Blueprint,request
from flask_restx import Resource,Api
from database.models import Card

bp = Blueprint('card',__name__)
api = Api(bp)

card_model = api.parser()
card_model.add_argument('card_number',type = str,required = True)
card_model.add_argument('user_id',type = int,required = True)
card_model.add_argument('amount',type = float,required = True)
card_model.add_argument('exp_date',type = str ,required = False)
card_model.add_argument('added_date',type = str ,required = False)


@api.route('/add-card')
class AddCart(Resource):
    @api.expect(card_model)
    def post(self):
        response = request.json

        card_number = response.get('card_number')
        user_id = response.get('user_id')
        amount = response.get('amount')
        exp_date = response.get('exp_date')
        added_date = response.get('added_date')


        try:
            Card().register_card(card_number,user_id,amount,exp_date,added_date)
            return {'status':1,'message':'Карта успешно создана'}

        except:
            return {'status':0,'message':'Ошибка при создании карты'}
