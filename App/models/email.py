import datetime
from App.database import db
from sqlalchemy.sql import func

class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey('user.id'))
    mailingListID = db.Column(db.Integer, db.ForeignKey('mailing_list.id'))
    subject = db.Column(db.String(100))
    body = db.Column(db.Text())
    status = db.Column(db.String(10))
    date = db.Column(db.DateTime(timezone=True), default=func.now())

    def __init__(self, list, subject, body, status):
        self.mailingListID = list
        self.subject = subject
        self.body = body
        self.status = status

    def toDict(self):
        return{
            'id': self.id,
            'userID': self.userID,
            'subject': self.subject,
            'body': self.body,
            'status': self.status,
            'date': self.date,
            'mailingListID': self.mailingListID,
        }

