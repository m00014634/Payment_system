from flask import Blueprint
from flask_restx import Api,Resource

bp = Blueprint('register',__name__)

api = Api(bp)


register_model = api.parser()
register_model.add_argument('name',type = str,required = True)
register_model.add_argument('phone_number',type = str,required = True)


@api.route('/register')
class Register(Resource):
    @api.expect(register_model)
    def post(self):
        pass
