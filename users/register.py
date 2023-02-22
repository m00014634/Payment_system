from flask import Blueprint,request
from flask_restx import Api,Resource
from database.models import User

bp = Blueprint('register',__name__)

api = Api(bp)


register_model = api.parser()
register_model.add_argument('name',type = str,required = True)
register_model.add_argument('phone_number',type = str,required = True)



@api.route('/register')
class RegisterUser(Resource):
    @api.expect(register_model) # User registration
    def post(self):
        response = register_model.parse_args()

        username = response.get('name')
        user_phone_number = response.get('phone_number')


        user_id = User().resister_user(username=username,user_phone_number = user_phone_number)
        return {'status':1,'user_id':user_id}



