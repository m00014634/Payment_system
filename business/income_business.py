
from flask_restx import Api,Resource
from database.models import Business,Payment
from business import api



income_model = api.parser()
income_model.add_argument('user_id',type=int,required = True)


@api.route('/income')
class GetBusinessIncome(Resource):
    @api.expect(income_model)
    def get(self):
        args = income_model.parse_args()
        user_id = args.get('user_id')

        business_to_get = Business.query.get(user_id)
        incomes = Payment().monitor_pays(business_to_get) #business_card

        return {'status':1,'message':incomes}