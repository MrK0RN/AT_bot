from imap_tools import MailBox, AND

from bs4 import BeautifulSoup
import re


class reader:
    def __init__(self):
        self.imap_server = "imap.rambler.ru"
        self.mails = []
        self.mp = []

    @staticmethod
    def parse_link(username, msg):
        soup = BeautifulSoup(msg.html).prettify()
        r = re.search(r"https://author.today/account/confirmEmail\S*\"", soup).group()[:-1]
        return username, r

    @staticmethod
    def get_mails():
        lines = []
        mails = []
        mp = []
        with open("../temp/accs", "r") as f:
            lines = f.read().split("\n")
        for i in lines:
            print(i)
            mails.append(i.split("|")[1])
        with open("../temp/mails/mails", "r") as f:
            lines = f.read().split("\n")
        for i in lines:
            j = i.split("|")
            if mails.count(j[0]):
                mp.append(j)
        return mp
    def read_mails(self, username, mail_pass):
        res = []
        with MailBox(self.imap_server, port=993).login(username, mail_pass) as mailbox:
            for msg in mailbox.fetch():
                if msg.from_ == "no-reply@author.today":
                    return self.parse_link()


    def delete_mails(self, username, mail_pass):
        with MailBox(self.imap_server, port=993).login(username, mail_pass) as mailbox:
            uids = []
            for msg in mailbox.fetch():
                if msg.from_ == "no-reply@author.today":
                    uids.append(msg.uid)
            mailbox.delete(uids)

def get_links():
    readerT = reader()
    mailpassword = readerT.get_mails()
    res = {}
    for i in mailpassword:
        g = readerT.read_mails(i[0], i[1])
        print("!")
        if g:
            mail, link = g
            res[mail] = link
    return res

def delete_links():
    readerT = reader()
    mailpassword = readerT.get_mails()
    res = {}
    for i in mailpassword:
        g = readerT.delete_mails(i[0], i[1])


