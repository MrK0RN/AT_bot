import data_transfer

db_user = "alexanderkrasnykh"
db_password = ""
db_name = "alexanderkrasnykh"
db_port = "5436"
db_host = "127.0.0.1"

from postgress import Pg8000DB

def sql(db_user, db_password, db_name, db_port):
    with open("all.sql", "r") as f:
        queries = f.read().split("\n")

    db = Pg8000DB(user=db_user, password=db_password, database=db_name, port=db_port, host=db_host)
    try:
        g = queries.pop(0)
        print(g)
        db.execute(g)
        print("complete")
    except Exception:
        print(Exception)
    db.close()
    db = Pg8000DB(user=db_user, password=db_password, database="at", port=db_port, host=db_host)
    for query in queries:
        try:
            print(query)
            db.execute(query)
            print("complete")
        except Exception:
            print(Exception)

sql(db_user, db_password, db_name, db_port)

db_name = "at"

db = Pg8000DB(user=db_user, password=db_password, database=db_name, port=db_port, host=db_host)

data_transfer.base_mail_transfer(db)

data_transfer.account_transfer(db)