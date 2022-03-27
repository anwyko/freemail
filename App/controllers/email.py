from flask_mail import Mail, Message

mail = Mail()

def init_email(app):
    mail.init_app(app)

def create_email(sender, receiver, title, body):
    email = Email(sender, receiver, title, body)
    
def send_email():
    msg = Message("Hey", sender = "info2601@accesstt.com", recipients = ["anwyko.trim@gmail.com"])
    msg.body = "Test email"
    mail.send(msg)

def send_bulk(list):
    with mail.connect() as conn:
        for user in list:
            message = '...'
            subject = "hello, %s" % user.name
            msg = Message(recipients=[user.email], body=message, subject=subject)
            conn.send(msg)
