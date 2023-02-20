from flask import Blueprint

from . import card, delete_usercard, expenses, payment , register, transfer

bp = Blueprint('user-pay',__name__,url_prefix='/user')

bp.register_blueprint(card.bp)
bp.register_blueprint(delete_usercard.bp)
bp.register_blueprint(expenses.bp)
bp.register_blueprint(payment.bp)
bp.register_blueprint(register.bp)
bp.register_blueprint(transfer.bp)