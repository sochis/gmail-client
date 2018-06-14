from gmail.mail import MailOperaton


class Execute():

    def search_gmail(self, query):
        mails = self.getmail.get_all_attribute(query)
        for mail in mails:
            print('Title : ' + mail['subject'])
            print('From : ' + mail['from'])
            print('To : ' + mail['to'])
            print('text : ' + mail['body'] + '\n')
            print('------------------------------------------------------------------------------------')

    def __init__(self):
        self.getmail = MailOperaton()


if __name__ == '__main__':
    execute = Execute()
    print('Input word that you want to search on gmail.')
    query = input()
    execute.search_gmail(query)
