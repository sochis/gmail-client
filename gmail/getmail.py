from auth.authorization import Credential
import base64
import sys


class GetMailContent():

    def get_id_and_titles(self):
        values = []
        messages = self.__get_mail_list('is:read OR is:unread')['messages']
        for message in messages:
            headers = self.__get_mail_content(message['id'])['payload']['headers']
            for header in headers:
                if header['name'] == 'Subject':
                    values.append(message['id'] + ' : ' + header['value'])
        return values

    def get_all_attribute(self, query):
        mail = []
        try:
            messages = self.__get_mail_list(query)['messages']
        except KeyError:
            print('No result found.')
            sys.exit()
        for message in messages:
            content = self.__get_mail_content(message['id'])
            values = self.__get_mail_all_attribute(content)
            mail.append(values)
        return mail

    def __get_mail_list(self, query):
        return self.service.users().messages().list(userId='me', q=query).execute()

    def __get_mail_content(self, id):
        return self.service.users().messages().get(userId='me', id=id).execute()

    def __get_mail_headers(self, query, name):
        header_values = []

        messages = self.__get_mail_list(query)['messages']
        for message in messages:
            content_headers = self.__get_mail_content(message['id'])['payload']['headers']
            for header in content_headers:
                if header['name'] == name:
                    header_values.append(header['value'])

        return header_values

    def __get_mail_all_attribute(self, content):
        mail = {}

        if 'parts' in content['payload'].keys():
            if 'data' in content['payload']['parts'][0]['body'].keys():
                raw_body = content['payload']['parts'][0]['body']['data']
            else:
                raw_body = ''
        else:
            raw_body = content['payload']['body']['data']
        mail['body'] = base64.urlsafe_b64decode(raw_body).decode('utf-8')
        mail['snippet'] = content['snippet']

        headers = content['payload']['headers']
        for header in headers:
            if header['name'] == 'From':
                mail['from'] = header['value']
            elif header['name'] == 'To':
                mail['to'] = header['value']
            elif header['name'] == 'Subject':
                mail['subject'] = header['value']
            elif header['name'] == 'Date':
                mail['date'] = header['value']
        return mail

    def __init__(self):
        self.service = Credential().readonly_credential()
