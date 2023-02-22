from flask import Blueprint,request
from flask_restx import Api,Resource
from database.models import User

bp = Blueprint('register',__name__)

api = Api(bp)


register_model = api.parser()
register_model.add_argument('name',type = str,required = True)
register_model.add_argument('phone_number',type = str,required = True)



@api.route('/register')
class Register(Resource):
    @api.expect(register_model) # User registration
    def post(self):
        response = request.json

        username = response.get('name')
        phone_number = response.get('phone_number')

        try:
            User().resister_user(username=username,phone_number=phone_number)
            return {'status':1,'message':'Пользователь успешно зарегистрирован'}
        except:
            return {'status':0,'message':'Такой пользователь уже существует'}


