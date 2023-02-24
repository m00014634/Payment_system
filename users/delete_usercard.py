from flask_restx import Api,Resource
from database.models import Card
from users import api

delete_usercard_model = api.parser()
delete_usercard_model.add_argument('card_number',type = int)



@api.route('/delete-card')
class DeleteCard(Resource):
    @api.expect(delete_usercard_model)
    def delete(self):

        current_usercard = delete_usercard_model.parse_args()
        if current_usercard:
            Card().delete_card(current_usercard.get('card_number'))
            return {'status':1,'message':'Карта успешно удалена'}

        return {'status':0,'message':'Карта не удалена'}