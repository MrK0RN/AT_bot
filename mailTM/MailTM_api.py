import requests
import config
from message import message


class mailtm:

    def __init__(self):
        self.raw_messages = None
        self.messages = []
        self.token = None
        self.id = None
        self.all_messages = {}

    def get_token_id(self, email, passw):
        url = config.server+"/token"

        data = {
            "address": email,
            "password": passw
        }
        response = requests.post(url, headers=config.headers, json=data)
        if response.status_code == 200:
            res = response.json()
        else:
            res = "error:\n" + str(response.status_code)
            print(res)

        self.token = res.get("token")
        self.id = res.get("id")

        return res

    def get_messages(self):
        url = config.server + "/messages"

        data = {
            #"id": self.id
            "page": 1
        }
        head = config.headers
        head["Authorization"] = "Bearer" + " " + self.token
        responce = requests.get(url, headers=config.headers, params=data)

        self.raw_messages = responce.json()
        for i in self.raw_messages:
            msg = message(i)
            self.messages.append(msg)
        return self.messages

    def check_new_messages(self):
        result = []
        for i in self.messages:
            if not(self.all_messages.setdefault(i.id, False)):
                result.append(i)
        return result

    def update_all_messages(self, msg=None):
        h = self.messages
        if msg:
            h = msg
        for i in h:
            self.all_messages[i.id] = i

        return self.all_messages


