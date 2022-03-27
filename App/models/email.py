from App.database import db

class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender =  db.Column(db.String, nullable=False)
    receiver = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    body = db.Column(db.String, nullable=False)

    def __init__(self, sender, receiver, title, body):
        self.sender = sender
        self.receiver = receiver
        self.title = title
        self.body = body

    def toDict(self):
        return{
            'sender': self.sender,
            'receiver': self.receiver,
            'title': self.title,
            'body': self.body,
        }

