from MailTM_api import mailtm

def parse_mails():
    mails = []
    with open("mails/mails", "r") as f:
        g = f.read().split("\n")
        for i in g:
            h = i.split(":")
            mails.append({
                "mail": h[0],
                "pass": h[1]
            })
    return mails

mails = parse_mails()

mailer = mailtm()
mailer.get_token_id(mails[0].get("mail"), mails[0].get("pass"))
print(mailer.id)
print(mailer.token)
mailer.get_messages()
#mailer.check_new_messages()
mailer.update_all_messages()