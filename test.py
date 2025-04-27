import postgress

db = postgress.Pg8000DB("postgres", "alexanderkrasnykh", "")
print("23e23e3e134134134")
#db.execute("CREATE USER davide WITH PASSWORD 'jw8s0F4';")
print("###########")
db.execute("CREATE DATABASE AuthorToday")
db.execute("CREATE TABLE accounts (id SERIAL PRIMARY KEY, name varchar(40) NOT NULL, email varchar(32) NOT NULL, acc_password varchar(12) NOT NULL, email_password varchar(12) NOT NULL, is_reged boolean NULL, is_authed boolean NULL)")
