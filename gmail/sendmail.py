from auth.authorization import Credential
from gmail.draft import Draft


class SendUtils():

    def send_draft(self):
        self.service.users().drafts().send('me')

    def send_mail(self, sender, receiver, subject, text):
        message_body = Draft().create_message(sender, receiver, subject, text)
        self.service.users().messages().send(userId='me', body=message_body).execute()

    def __init__(self):
        self.service = Credential().modify_credential()
