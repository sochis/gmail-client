from auth import authorization
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.audio import MIMEAudio
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
import mimetypes
import base64
import os


class DraftOperation():

    def create_draft(self, message_body):
        message = {'message': message_body}
        self.service.users().drafts().create(userId='me', body=message).execute()

    def create_message(self, sender, receiver, subject, text):
        message = MIMEText(text)
        message['from'] = sender
        message['to'] = receiver
        message['subject'] = subject
        b64_string = base64.urlsafe_b64encode(message.as_bytes()).decode()
        return {'raw': b64_string}

    def create_message_with_attachment(self, sender, receiver, subject, text, file_dir, filename):
        message = MIMEMultipart()
        message['from'] = sender
        message['to'] = receiver
        message['subject'] = subject
        msg = MIMEText(text)
        message.attach(msg)

        path = os.path.join(file_dir, filename)
        content_type, encoding = mimetypes.guess_type(path)

        if (content_type is None or encoding is not None):
            content_type = 'application/octet-stream'

        main_type, sub_type = content_type.split('/', 1)
        if (main_type == 'text'):
            file = open(path, 'rb')
            msg = MIMEText(file.read(), _subtype=sub_type)
            file.close()
        elif (main_type == 'audio'):
            file = open(path, 'rb')
            msg = MIMEAudio(file.read(), _subtype=sub_type)
            file.close()
        elif (main_type == 'image'):
            file = open(path, 'rb')
            msg = MIMEImage(file.read(), _subtype=sub_type)
            file.close()
        else:
            file = open(path, 'rb')
            msg = MIMEBase(main_type, sub_type)
            msg.set_payload(file.read())
            file.close()

        msg.add_header('Content-Disposition', 'attachment', filename=filename)
        message_body = base64.urlsafe_b64encode(message.as_bytes()).decode()

        return {'raw': message_body}

    def modify_draft(self, draft_id, sender, receiver, subject, text):
        message = self.create_message(sender, receiver, subject, text)
        self.service.users().drafts().update(userId='me', id=draft_id, body=message).execute()

    def send_draft(self, draft_id):
        self.service.users().drafts().send(userId='me', id=draft_id).execute()

    def delete_draft(self, draft_id):
        self.service.users().drafts().delete(userId='me', id=draft_id).execute()
        print('Draft with id: %s deleted successfully.' % draft_id)

    def get_ids(self):
        values = []
        messages = self.__get_draft_list('is:read OR is:unread')['drafts']
        for message in messages:
            values.append(message['message']['id'])
        return values

    def __get_draft_list(self, query):
        return self.service.users().drafts().list(userId='me', q=query).execute()

    def __get_draft_content(self, draft_id):
        return self.service.users().drafts().get(id=draft_id, userId='me').execute()

    def __init__(self):
        self.service = authorization.Credential().full_credential()
