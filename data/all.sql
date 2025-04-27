CREATE DATABASE AT
CREATE TABLE accounts (id SERIAL PRIMARY KEY, name varchar(60) NOT NULL, email varchar(32) NOT NULL, acc_password varchar(20) NOT NULL, email_password varchar(20) NOT NULL, is_reged boolean NULL, is_authed boolean NULL);
CREATE TABLE authentification_links(id SERIAL PRIMARY KEY, email varchar(32) NOT NULL, authentification_links varchar(255) NOT NULL, tryed boolean NULL);
CREATE TABLE mails (id SERIAL PRIMARY KEY, mail varchar(32), password varchar(20), used boolean NOT NULL);