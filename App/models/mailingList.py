from App.database import db

mailing_list_recipient = db.Table('mailing_list_recipient',
    db.Column('mailing_list_id', db.Integer, db.ForeignKey('mailing_list.id')),
    db.Column('recipient_id', db.Integer, db.ForeignKey('recipient.id'))
)

class MailingList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    userID = db.Column(db.Integer, db.ForeignKey('user.id'))
    recipients = db.relationship('Recipient', secondary='mailing_list_recipient', backref='mailinglists')
    emails = db.relationship('Email', backref='mailingList')

    def __init__(self, name):
        self.name = name

    def toDict(self):
        return{
            'id': self.id,
            'userId': self.userID,
            'name': self.name,
        }

