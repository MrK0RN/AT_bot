import data

def email_is_used(email):
    db = data.postgress.usual_db()
    res = db.execute(f"UPDATE mail SET used = {True} WHERE mail = {email} ")

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
