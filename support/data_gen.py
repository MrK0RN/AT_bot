from support.passw_gen import gen as genh
from mimesis import Person
from support.data_operate import give_unused_email

person = Person('ru')

def gen():
    fio = person.full_name()
    passw = genh(8)
    email = give_unused_email()
    return fio, email, passw