from flask_mail import Mail, Message
from App.models import *
from App.database import db


mail = Mail()

def init_email(app):
    mail.init_app(app)

def get_all_emails():
    return Email.query.all()

def get_email(emailID):
    return Email.query.filter_by(id=emailID).first()

def get_all_emails_json():
    emails = Email.query.all()
    if not emails:
        return []
    emails = [email.toDict() for email in emails]
    return emails

def get_email_json(emailID):
    email = Email.query.filter_by(id=emailID).first()
    if not email:
        return False
    return email.toDict()

def delete_email(emailID):
    email = Email.query.filter_by(id=emailID).first()
    if email == None:
        return False
    db.session.delete(email)
    db.session.commit()
    return True

def update_email(emailID, mailingList, subject, body):
    email = Email.query.filter_by(id=emailID).first()
    if email == None:
        return False
    email.mailingList = mailingList
    email.subject = subject
    email.body = body
    db.session.add(email)
    db.session.commit()
    return True

def create_email(subject, body, status):
    email = Email(subject, body, status)
    db.session.add(email)
    db.session.commit()

def add_list_to_email(emailID, listID):
    mlist = MailingList.query.filter_by(id=listID).first()
    email = Email.query.filter_by(id=emailID).first()
    email.mailingList = mlist
    db.session.commit()

def remove_list_from_email(emailID, listID):
    mlist = MailingList.query.filter_by(id=listID).first()
    email = Email.query.filter_by(id=emailID).first()
    mlist.emails.remove(email)
    db.session.commit()
    
def send_email():
    msg = Message("Hey", sender = "info2601@accesstt.com", recipients = ["anwyko.trim@gmail.com"])
    msg.body = "Test email"
    mail.send(msg)

#add check
def send_bulk(emailID):
    email = Email.query.filter_by(id=emailID).first()
    with mail.connect() as conn:
        for recipient in email.mailingList.recipients:
            subject = email.subject
            body = email.body
            message = Message(sender="info2601@accesstt.com", recipients=[recipient.email], body=body, subject=subject)
            conn.send(message)

