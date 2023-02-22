from flask import Blueprint
from flask_restx import Api,Resource

bp = Blueprint('expenses',__name__)
api = Api(bp)

expenses_model = api.parser()
expenses_model.add_argument('amount',type = float)
expenses_model.add_argument('service_type',type = str)



@api.route('/expenses')
class Expenses(Resource):
    @api.expect(expenses_model)
    def post(self):
        return ''