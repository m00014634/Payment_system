
from flask_restx import Api,Resource
from database.models import Payment

from users import api

expenses_model = api.parser()
expenses_model.add_argument('card_number',type = str)



@api.route('/expenses')
class Expenses(Resource):
    @api.expect(expenses_model)
    def get(self):
        card_number = expenses_model.parse_args()

        result = Payment().monitor_pays(card_number.get('card_number'))

        if result:
            return {'status':1,'message':result}

        return {'status':0,'message':'Ничего не найдено'}