import os
from flask import Flask, request, redirect, url_for
from flask_login import LoginManager, current_user
from flask_uploads import DOCUMENTS, IMAGES, TEXT, UploadSet, configure_uploads
from flask_cors import CORS
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from datetime import timedelta


from App.database import create_db, get_migrate

from App.controllers import *
# (
#     setup_jwt,
#     init_email,
#     create_recipients_from_csv
# )

from App.views import (
    user_views,
    email_views,
    list_views,
    recipient_views,
    api_views
)

from App.models import *

views = [
    user_views,
    email_views,
    list_views,
    recipient_views,
    api_views
]

def add_views(app, views):
    for view in views:
        app.register_blueprint(view)


def loadConfig(app, config):
    app.config['ENV'] = os.environ.get('ENV', 'DEVELOPMENT')
    if app.config['ENV'] == "DEVELOPMENT":
        app.config.from_object('App.config')
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
        app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
        app.config['JWT_EXPIRATION_DELTA'] =  timedelta(days=int(os.environ.get('JWT_EXPIRATION_DELTA')))
        app.config['DEBUG'] = os.environ.get('ENV').upper() != 'PRODUCTION'
        app.config['ENV'] = os.environ.get('ENV')
    for key, value in config.items():
        app.config[key] = config[key]

def create_app(config={}):
    app = Flask(__name__, static_url_path='/static')
    CORS(app)
    loadConfig(app, config)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['PREFERRED_URL_SCHEME'] = 'https'
    app.config['UPLOADED_PHOTOS_DEST'] = "App/uploads"
    photos = UploadSet('photos', TEXT + DOCUMENTS + IMAGES)
    configure_uploads(app, photos)
    add_views(app, views)
    create_db(app)
    setup_jwt(app)
    init_email(app)
    app.app_context().push()
    return app

app = create_app()
migrate = get_migrate(app)

@app.route("/upload", methods=['POST'])
def uploadFiles():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        file_path = os.path.join(app.config['UPLOADED_PHOTOS_DEST'], uploaded_file.filename)
        uploaded_file.save(file_path)
        create_recipients_from_csv(file_path)
    return redirect(url_for('recipient_views.get_recipients_api'))

def populate_db():
    db.session.add_all([
    User(username="bob", password="bobpass"),
    Email(subject="subject1", body="body1", status="draft"),
    Email(subject="subject2", body="body2", status="draft"),
    Email(subject="subject3", body="body3", status="draft"),
    Email(subject="subject4", body="body4", status="sent"),
    Email(subject="subject5", body="body5", status="sent"),
    MailingList(name="name1"),
    MailingList(name="name2"),
    MailingList(name="name3"),
    Recipient(firstName="firstName1", lastName="lastName1", email="email1"),
    Recipient(firstName="firstName2", lastName="lastName2", email="email2"),
    Recipient(firstName="firstName3", lastName="lastName3", email="email3"),
    Recipient(firstName="firstName4", lastName="lastName4", email="email4"),
    Recipient(firstName="firstName5", lastName="lastName5", email="email5"),
    Recipient(firstName="firstName6", lastName="lastName6", email="email6"),
    Recipient(firstName="firstName7", lastName="lastName7", email="email7"),
    Recipient(firstName="firstName8", lastName="lastName8", email="email8"),
    Recipient(firstName="firstName9", lastName="lastName9", email="email9"),
    Recipient(firstName="firstName10", lastName="lastName10", email="email10")])
    db.session.commit()
    user = User.query.first()
    emails = Email.query.all()
    lists = MailingList.query.all()
    recipients = Recipient.query.all()
    add_list_to_user(user.id, lists[0].id)
    add_list_to_user(user.id, lists[1].id)
    add_list_to_user(user.id, lists[2].id)
    add_email_to_user(user.id, emails[0].id)
    add_email_to_user(user.id, emails[1].id)
    add_email_to_user(user.id, emails[2].id)
    add_email_to_user(user.id, emails[3].id)
    add_email_to_user(user.id, emails[4].id)
    add_list_to_email(emails[0].id, lists[0].id)
    add_list_to_email(emails[1].id, lists[1].id)
    add_list_to_email(emails[2].id, lists[2].id)
    add_list_to_email(emails[3].id, lists[0].id)
    add_list_to_email(emails[4].id, lists[1].id)
    add_recipient_to_list(lists[0].id, recipients[0].id)
    add_recipient_to_list(lists[1].id, recipients[1].id)
    add_recipient_to_list(lists[2].id, recipients[2].id)
    add_recipient_to_list(lists[0].id, recipients[3].id)
    add_recipient_to_list(lists[1].id, recipients[4].id)
    add_recipient_to_list(lists[2].id, recipients[5].id)
    add_recipient_to_list(lists[0].id, recipients[6].id)
    add_recipient_to_list(lists[1].id, recipients[7].id)
    add_recipient_to_list(lists[2].id, recipients[8].id)
    add_recipient_to_list(lists[0].id, recipients[9].id)
    db.session.commit()

