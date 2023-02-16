from flask import Blueprint
from flask_restx import Resource,Api


bp = Blueprint('cabinet',__name__)
api = Api(bp)

model_service_register = api.parser()
model_service_register.add_argument('user_id',type=int,required =True)
model_service_register.add_argument('service_name',type= str,required =True)
model_service_register.add_argument('service_type',type= str,required =True)
model_service_register.add_argument('which_card',type= int,required =True)

@api.route('/add-service')
class AddService(Resource):

    @api.expect(model_service_register)
    def post(self):
        pass
