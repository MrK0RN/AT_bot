from passw_gen import gen as genh
from mimesis import Person

person = Person('ru')

mails = []

with open("mails/unused", "r") as f:
    g = f.read().split("\n")
    for i in g:
        h = i.split("|")
        print(h)
        mails.append({
            "mail": h[0],
            "pass": h[1]
        })


def gen():
    ms = ""
    fio = person.full_name()
    email = mails.pop(0)["mail"]
    passw = genh(8)
    for i in mails:
        ms += i.get("mail") + "|" + i.get("pass")+"\n"
    ms = ms[:-1]
    with open("mails/unused", "w") as f:
        f.write(ms)
    with open("mails/used", "a") as f:
        f.write(email)
    with open("accs", "a") as f:
        f.write(fio + "|" + email + "|" + passw+"\n")
    return fio, email, passw

#authModal > div > div > div:nth-child(2) > form:nth-child(1) > button
#/html/body/div[1]/div/section/div/div/div/div[2]/form[1]/button