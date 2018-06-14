from gmail.mail import MailOperaton
from gmail.draft import DraftOperation
import sys


class Send():

    def send_draft(self):
        print('Input draft ID of sending target mail')
        draft_id = input()
        DraftOperation().send_draft(draft_id)
        print('\nDraft is sent normally.')

    def send_mail(self):
        print('Input the mailing address.')
        receiver = input()
        print('Input your gmail address.')
        sender = input()
        print('Input the subject.')
        subject = input()
        print('Input the text.')
        text = input()
        MailOperaton().send_mail(sender, receiver, subject, text)
        print('\nMail is sent to "' + receiver + '"')


if __name__ == '__main__':
    print("What kind of ID do you want to send? ('mail'/'draft')")
    type = input()
    execute = Send()
    if type == 'mail':
        execute.send_mail()
    elif type == 'draft':
        execute.send_draft()
    else:
        print('Input word is invalid.')
        sys.exit()