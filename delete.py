from gmail.mail import MailOperaton
from gmail.draft import DraftOperation
import sys

class Delete():

    def delete_draft(self):
        print('Input draft ID that you want to delete.')
        draft_id = input()
        DraftOperation().delete_draft(draft_id)

    def delete_mail(self):
        print('Input mail ID that you want to delete.')
        mail_id = input()
        MailOperaton().delete_mail(mail_id)


if __name__ == '__main__':
    delete = Delete()
    print("What kind of ID do you want to delete? ('mail'/'draft')")
    type = input()
    if type == 'draft':
        delete.delete_draft()
    elif type == 'mail':
        delete.delete_mail()
    else:
        print('Input word is invalid.')
        sys.exit()