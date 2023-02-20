from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from business import bp as business_bp
from users import bp as users_bp

app = Flask(__name__)
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pay.db'
db.init_app(app)


app.register_blueprint(business_bp)
app.register_blueprint(users_bp)


@app.route('/')
def hello():
    return 'Salom'


app.run()