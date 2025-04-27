import data.postgress

def email_is_used(email):
    db = data.postgress.usual_db()
    res = db.execute(f"UPDATE mail SET used = {True} WHERE mail = \'{email}\'")

def create_account(name, mail, password, is_reged):
    db = data.postgress.usual_db()
    query = f'SELECT password FROM mails WHERE mail=\'{mail}\''
    g = db.execute(query, fetch=True)
    query = f'INSERT INTO accounts (name, email, acc_password, email_password, is_reged, is_authed) VALUES (\'{name}\', \'{mail}\', \'{password}\', \'{g[0][0]}\', {is_reged}, {False})'
    db.execute(query)

def give_unused_email():
    db = data.postgress.usual_db()
    res = db.execute(f"SELECT mail FROM mails WHERE used = {False}", fetch=True)
    return res[0][0]

def load_links(mail):
    db = data.postgress.usual_db()
    print(mail)
    for i in mail:
        db.execute(f"INSERT INTO authentification_links (email, authentification_links, tryed) VALUES (\'{i}\', \'{mail[i]}\', {False})")

def parse_links():
    db = data.postgress.usual_db()
    res = db.execute(f"SELECT * FROM authentification_links WHERE tryed = {False}", fetch=True)
    print(res)
    return res

def get_accounts(mail=None):
    db = data.postgress.usual_db()
    if mail:
        res = db.execute(f"SELECT * FROM accounts WHERE email = \'{mail}\'", fetch=True)
    else:
        res = db.execute(f"SELECT * FROM accounts", fetch=True)
    return res