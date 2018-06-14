from gmail.draft import DraftOperation


class Execute():

    def create_draft(self, sender, receiver, subject, text):
        message_body = self.draft.create_message(sender, receiver, subject, text)
        self.draft.create_draft(message_body)

    def create_draft_with_attachment(self, sender, receiver, subject, text, file_dir, filename):
        try:
            message_body = self.draft.create_message_with_attachment(sender, receiver, subject, text, file_dir, filename)
        except (NameError, FileNotFoundError):
            print("Directory or file name isn't correct. This step is skipped.")
            message_body = self.draft.create_message(sender, receiver, subject, text)
        self.draft.create_draft(message_body)

    def __init__(self):
        self.draft = DraftOperation()


if __name__ == '__main__':
    execute = Execute()
    print('Input the mailing address.')
    receiver = input()
    print('Input your gmail address.')
    sender = input()
    print('Input the subject.')
    subject = input()
    print('Input the text.')
    text = input()
    print('Do you want to attach file? (y/n)')
    answer = input()
    flag = 1
    file_dir = ''
    filename = ''
    while (flag == 1):
        if (answer == 'y'):
            print('Input target file directory.')
            file_dir = input()
            print('Input target file name.')
            filename = input()
            flag = 0
        elif (answer == 'n'):
            print('This step is skipped.')
            flag = 0
        else:
            print("Argument isn't correct. Input 'y' or 'n'")
            answer = input()
    execute.create_draft_with_attachment(sender, receiver, subject, text, file_dir, filename)
    print('Draft is created.')
