from support.passw_gen import gen as genh
from mimesis import Person
import data_operate

person = Person('ru')

def gen():
    fio = person.full_name()
    passw = genh(8)
    email = data_operate.give_unused_email()
    return fio, email, passw