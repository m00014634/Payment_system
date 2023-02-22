from flask import Blueprint
from flask_restx import Api,Resource
from database.models import Card

bp = Blueprint('delete_usercard',__name__)
api = Api(bp)

delete_usercard_model = api.parser()
delete_usercard_model.add_argument('card_number',type = int)
delete_usercard_model.add_argument('user_id',type = int)



@api.route('/delete-card')
class Expenses(Resource):
    @api.expect(delete_usercard_model)
    def delete(self,card_id):
        current_usercard = Card.query.get_or_404(card_id)

        if current_usercard:
            Card.delete_card(current_usercard,card_id)
            return {'status':1,'message':'Карта успешно удалена'}

        return {'status':0,'message':'Карта не удалена'}