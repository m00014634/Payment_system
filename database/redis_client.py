from redis import Redis
import random


class RedisDb:
    def __init__(self,host='localhost',port=6379,db=0):
        self.redis_side = Redis(host=host,port=port,db=db)

    #Одноразовые генерации кодов подтверждения
    def generate_verify_code(self,user_phone_number):
        verif_code= random.randint(1212,9999)

        #Создаем временный ключ на 60 секунд
        self.redis_side.set(user_phone_number,verif_code,60)


        return verif_code

    #Проверка кода
    def check_verif_code(self,user_phone_number,user_input):
        # Получаем значение отправленное пользователю по номеру
        checker = self.redis_side.get(user_phone_number)

        if checker and checker == user_input:
            return True

        return False