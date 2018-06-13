from gmail.draft import Draft


class Execute():

    def create_draft(self, sender, receiver, subject, text):
        message_body = self.draft.create_message(sender, receiver, subject, text)
        self.draft.create_draft(message_body)

    def __init__(self):
        self.draft = Draft()


if __name__ == '__main__':
    execute = Execute()
    print('Input your gmail address.')
    sender = input()
    print('Input the mailing address.')
    receiver = input()
    print('Input the subject.')
    subject = input()
    print('Input the text.')
    text = input()
    print('Input the path to file if you want to attach the file.')
    attachment = input()
    execute.create_draft(sender, receiver, subject, text)
    print('Draft is created.')
