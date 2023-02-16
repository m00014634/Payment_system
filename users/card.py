from flask import Blueprint
from flask_restx import Resource,Api

bp =Blueprint('card',__name__)
api = Api(bp)

card_model = api.parser()
card_model.add_argument('card_number',type = str,required = True)
card_model.add_argument('name',type = str,required = True)
card_model.add_argument('phone_number',type = str,required = True)


@api.route('/add-card')
class AddCart(Resource):
    @api.expect(card_model)
    def post(self):
        pass