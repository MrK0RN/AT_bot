from imap_tools import MailBox, AND

from email.header import decode_header
import base64
from bs4 import BeautifulSoup
import re

def get_mails():
    lines = []
    mails = []
    mp = []
    with open("accs", "r") as f:
        lines = f.read().split("\n")
    for i in lines:
        print(i)
        mails.append(i.split("|")[1])
    with open("mails/mails", "r") as f:
        lines = f.read().split("\n")
    for i in lines:
        j = i.split("|")
        if mails.count(j[0]):
            mp.append(j)
    return mp

class reader:
    def __init__(self):
        self.imap_server = "imap.rambler.ru"
        self.mails = []
        self.mp = []

    def read_mails(self, username, mail_pass):
        res = []
        with MailBox(self.imap_server, port=993).login(username, mail_pass) as mailbox:
            for msg in mailbox.fetch():
                if msg.from_ == "no-reply@author.today":
                    print(username)
                    soup = BeautifulSoup(msg.html).prettify()
                    r = re.search(r"https://author.today/account/confirmEmail\S*\"", soup).group()[:-1]
                    print(r)
                    return username, r


    def delete_mails(self, username, mail_pass):
        with MailBox(self.imap_server, port=993).login(username, mail_pass) as mailbox:
            uids = []
            for msg in mailbox.fetch():
                if msg.from_ == "no-reply@author.today":
                    print("######")
                    uids.append(msg.uid)
            mailbox.delete(uids)

def get_links():
    mp = get_mails()
    res = {}
    for i in mp:
        readerT = reader()
        g = readerT.read_mails(i[0], i[1])
        if g:
            h, k = g
            res[h] = k
    return res

def delete_links():
    mp = get_mails()
    res = {}
    for i in mp:
        readerT = reader()
        g = readerT.delete_mails(i[0], i[1])

delete_links()


