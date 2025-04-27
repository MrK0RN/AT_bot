#mail transfer

def base_mail_transfer(db, dir="mails", domen="@rambler.ru"):
    with open(dir+"/mails", "r") as f:
        mails = f.read().split("\n")
    with open(dir+"/used", "r") as f:
        mails_used = f.read().split(domen)
        mails_used.pop()
    print(len(mails))
    for mail in mails:
        mp = mail.split("|")
        isUsed = bool(mails_used.count(mail.split("@")[0]))
        query = f'INSERT INTO mails (mail, password, used) VALUES (\'{mp[0]}\', \'{mp[1]}\', {isUsed})'
        db.execute(query)

def account_transfer(db):
    with open("accs", "r") as f:
        accs = f.read().split("\n")

    for acc in accs:
        acc_s = acc.split("|")

        query = f'SELECT password FROM mails WHERE mail=\'{acc_s[1]}\''
        g = db.execute(query, fetch=True)
        query = f'INSERT INTO accounts (name, email, acc_password, email_password) VALUES (\'{acc_s[0]}\', \'{acc_s[1]}\', \'{acc_s[2]}\', \'{g[0][0]}\')'
        print(query)
        db.execute(query)
