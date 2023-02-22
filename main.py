from flask import Flask

from database.models import db
from flask_migrate import Migrate

import business
import users


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/pay'
db.init_app(app)

migrate = Migrate(app,db)


app.register_blueprint(users.card.bp,url_prefix = '/card')
app.register_blueprint(users.delete_usercard.bp,url_prefix = '/delete')
app.register_blueprint(users.expenses.bp,url_prefix = '/expenses')
app.register_blueprint(users.payment.bp,url_prefix = '/payment')
app.register_blueprint(users.register.bp,url_prefix = '/reg')
app.register_blueprint(users.transfer.bp,url_prefix = '/transfer')


app.register_blueprint(business.cabinet.bp,url_prefix = '/cabinet')
app.register_blueprint(business.income_business.bp,url_prefix = '/income_track')
app.register_blueprint(business.invoice_business.bp,url_prefix = '/invoices')



@app.route('/')
def hello():
    return 'Salom'


app.run()