'''
Code	Details
200
Response body
Download
{
  "@context": "/contexts/Message",
  "@id": "/messages",
  "@type": "hydra:Collection",
  "hydra:totalItems": 1,
  "hydra:member": [
    {
      "@id": "/messages/6807bf2eb4ec747cfae50a69",
      "@type": "Message",
      "id": "6807bf2eb4ec747cfae50a69",
      "msgid": "<CAH__Wq6cgoMv9g2kOECObc_4T_VRkE072b6Dbo2RSibdDxrYwA@mail.gmail.com>",
      "from": {
        "address": "vikmamoch123.1@gmail.com",
        "name": "Вилова Рина"
      },
      "to": [
        {
          "address": "rhxnrdjz@belgianairways.com",
          "name": ""
        }
      ],
      "subject": "",
      "intro": "idnwjvnqejpbvjqndvnqjdvnq wdwnveqfv Code: 235923",
      "seen": false,
      "isDeleted": false,
      "hasAttachments": false,
      "size": 3395,
      "downloadUrl": "/messages/6807bf2eb4ec747cfae50a69/download",
      "sourceUrl": "/sources/6807bf2eb4ec747cfae50a69",
      "createdAt": "2025-04-22T16:09:01+00:00",
      "updatedAt": "2025-04-22T16:09:18+00:00",
      "accountId": "/accounts/669eb23d343660b51e06c4f0"
    }
  ]
}
'''


class message:

    def __init__(self, message):
        self.id = message.get("id")
        self.msgid = message.get("msgid")
        self.mail_from = {
            "address": message.get("mail_from").get("address"),
            "name": message.get("mail_from").get("name")
        }
        self.mail_to = []
        for i in message.get("mail_from"):
            self.mail_to.append({
                "address": i.get("address"),
                "name": i.get("name")
            })

        self.subject = message.get('subject')
        self.intro = message.get('intro')
        self.seen = message.get('seen')
        self.isDeleted = message.get('isDeleted')
        self.hasAttachments = message.get('hasAttachments')
        self.size = message.get('size')
        self.downloadUrl = message.get('downloadUrl')
        self.sourceUrl = message.get('sourceUrl')
        self.createdAt = message.get('createdAt')
        self.updatedAt = message.get('updatedAt')
        self.accountId = message.get('accountId')

    def low(self):
        return self.id, self

    def download_message(self):
        pass
