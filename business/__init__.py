from flask import Blueprint

from . import cabinet, income_business , invoice_business

bp = Blueprint('for-business',__name__,url_prefix='/business')

bp.register_blueprint(cabinet.bp)
bp.register_blueprint(income_business.bp)
bp.register_blueprint(invoice_business.bp)