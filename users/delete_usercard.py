from flask import Blueprint
from flask_restx import Api,Resource

bp = Blueprint('delete_usercard',__name__)
api = Api(bp)

delete_usercard_model = api.parser()
delete_usercard_model.add_argument('card_number',type = int)
delete_usercard_model.add_argument('user_id',type = int)



@api.route('/delete-card')
class Expenses(Resource):
    @api.expect(delete_usercard_model)
    def delete(self):
        pass