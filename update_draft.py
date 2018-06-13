from gmail.draft import Draft

class Execute():

    def update_draft(self, draft_id, sender, receiver, subject, text):
        Draft().modify_draft(draft_id, sender, receiver, subject, text)


if __name__ == '__main__':
    print('Input draft id.')
    draft_id = input()
    print('Input your gmail address.')
    sender = input()
    print('Input the mailing address.')
    receiver = input()
    print('Input the subject.')
    subject = input()
    print('Input the text.')
    text = input()
    Execute().update_draft(draft_id, sender, receiver, subject, text)