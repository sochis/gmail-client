from gmail.sendmail import SendUtils

class Send():

    # def send_draft(self):

    def send_mail(self):
        print('Input the mailing address.')
        sender = input()
        print('Input your gmail address.')
        receiver = input()
        print('Input the subject.')
        subject = input()
        print('Input the text.')
        text = input()
        SendUtils().send_mail(sender, receiver, subject, text)


if __name__ == '__main__':
    execute = Send()
    execute.send_mail()