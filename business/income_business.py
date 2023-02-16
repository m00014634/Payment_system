from flask import Blueprint
from flask_restx import Api,Resource


bp = Blueprint('income',__name__)
api = Api(bp)


income_model = api.parser()
income_model.add_argument('user_id',type=int,required = True)


@api.route('/income')
class GetBusinessIncome(Resource):
    @api.expect(income_model)
    def get(self):
        pass