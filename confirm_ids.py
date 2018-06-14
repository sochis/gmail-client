from gmail.draft import DraftOperation
from gmail.mail import MailOperaton
import sys


class Confirm():

    def show_draft_ids(self):
        values = DraftOperation().get_ids()
        for value in values:
            print(value)

    def show_mail_id_and_titles(self):
        values = MailOperaton().get_id_and_titles()
        for value in values:
            print(value)


if __name__ == '__main__':
    print("What kind of ID do you want to see? ('mail'/'draft')")
    type = input()
    if type == 'mail':
        Confirm().show_mail_id_and_titles()
    elif type == 'draft':
        Confirm().show_draft_ids()
    else:
        print('Input word is invalid.')
        sys.exit()
