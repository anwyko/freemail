from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
import jwt

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(100))
    lastName = db.Column(db.String(100))
    username =  db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    emails = db.relationship('Email', backref='user')
    lists = db.relationship('MailingList', backref='user')

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def toDict(self):
        return{
            'id': self.id,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'username': self.username,
            'email': self.email,
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

# def encode_auth_token(self, user_id):
#     """
#     Generates the Auth Token
#     :return: string
#     """
#     try:
#         payload = {
#             'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
#             'iat': datetime.datetime.utcnow(),
#             'sub': user_id
#         }
#         return jwt.encode(
#             payload,
#             app.config.get('SECRET_KEY'),
#             algorithm='HS256'
#         )
#     except Exception as e:
#         return e

# @staticmethod
# def decode_auth_token(auth_token):
#     """
#     Decodes the auth token
#     :param auth_token:
#     :return: integer|string
#     """
#     try:
#         payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
#         return payload['sub']
#     except jwt.ExpiredSignatureError:
#         return 'Signature expired. Please log in again.'
#     except jwt.InvalidTokenError:
#         return 'Invalid token. Please log in again.'