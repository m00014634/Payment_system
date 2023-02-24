from flask import Blueprint

from flask_restx import Api

# from . import card, expenses,register,transfer

bp = Blueprint('users',__name__,url_prefix='/users')
api = Api(bp)

from . import card,expenses,register,transfer,delete_usercard