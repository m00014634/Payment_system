from datetime import datetime
from main import db


# Модель пользователя
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True,unique = True,authoincrement = True)
    user_phone_number = db.Column(db.String(11),unique = True,null = False)
    username = db.Column(db.String(75),null =False)
    reg_date = db.Column(db.DateTime,default = datetime.now())

    # Регистрация
    def resister_user(self,phone_number,username):
        pass


    # Изменить номер телефона
    def change_phone_number(self,user_id,new_phone_number):
        pass


# Модель карт
class Card(db.Model):
    __tablename__ = 'cards'
    id = db.Column(db.Integer,primary_key = True,unique = True,authoincrement = True)
    card_number = db.Column(db.Integer,unique = True,null =False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id',on_delete='SET NULL'))
    amount = db.Column(db.Float)
    exp_date = db.Dolumn(db.Date,null = False)
    added_date = db.Column(db.DateTime,default=datetime.now())



    # Регистрация карты


    # Удалить карту



# Модель платежей
class Payment(db.Model):
    __tablename__ = 'payments'
    id = db.Column(db.Integer,primary_key = True,unique = True, authoincrement = True)
    card_id = db.Column(db.Integer,db.ForeignKey('cards.id',on_delete = 'SET 0'),null = False)
    amount = db.Column(db.Float)
    pay_date = db.Column(db.DateTime,default = datetime.now())

    card = db.relationship('Card')

    # Создать платеж






# Модель бизнеса




# Модель сервиса




# Модель типа сервиса