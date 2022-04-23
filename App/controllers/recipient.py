from App.models import Email, User, Recipient
from App.database import db
import csv

def create_recipient(firstName, lastName, email):
    recipient = Recipient(firstName=firstName, lastName=lastName, email=email)
    db.session.add(recipient)
    db.session.commit()
    return recipient.id

def create_recipients_from_csv(file):
    with open(file) as f:
        reader = csv.DictReader(f)
        for row in reader:
            recipient = Recipient(firstName=row["firstName"], lastName=row["lastName"], email=row["email"])
            db.session.add(recipient)
        db.session.commit()

def get_all_recipients():
    return Recipient.query.all()

def get_recipient(recipientID):
    return Recipient.query.filter_by(id=recipientID).first()

def get_all_recipients_json():
    recipients = Recipient.query.all()
    if not recipients:
        return []
    recipients = [recipient.toDict() for recipient in recipients]
    return recipients

def get_recipient_json(recipientID):
    recipient = Recipient.query.filter_by(id=recipientID).first()
    if not recipient:
        return False
    return recipient.toDict()

def delete_recipient(recipientID):
    recipient = Recipient.query.filter_by(id=recipientID).first()
    if recipient == None:
        return False
    db.session.delete(recipient)
    db.session.commit()
    return True

def update_recipient(recipientID, firstName, lastName, email):
    recipient = Recipient.query.filter_by(id=recipientID).first()
    if recipient == None:
        return False
    recipient.firstName = firstName
    recipient.lastName = lastName
    recipient.email = email
    db.session.add(recipient)
    db.session.commit()
    return True