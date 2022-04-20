from App.models import *
from App.database import db


def get_all_users():
    return User.query.all()

def get_user(userID):
    return User.query.filter_by(id=userID).first()

def create_user(username, password):
    newuser = User(username=username, password=password)
    db.session.add(newuser)
    db.session.commit()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.toDict() for user in users]
    return users

def get_user_json(userID):
    user = User.query.filter_by(id=userID).first()
    if not user:
        return "User not found"
    return user.toDict()

def delete_user(userID):
    user = User.query.filter_by(id=userID).first()
    if user == None:
        return False
    db.session.delete(user)
    db.session.commit()
    return True

def update_user(userID, firstName, lastName, email):
    user = User.query.filter_by(id=userID).first()
    if user == None:
        return False
    user.firstName = firstName
    user.lastName = lastName
    user.email = email
    db.session.add(user)
    db.session.commit()
    return True

def change_password(userID, password):
    user = User.query.filter_by(id=userID).first()
    if user == None:
        return False
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return True

def add_email_to_user(userID, emailID):
    user = User.query.filter_by(id=userID).first()
    email = Email.query.filter_by(id=emailID).first()
    user.emails.append(email)
    db.session.commit()

def add_list_to_user(userID, listID):
    mlist = MailingList.query.filter_by(id=listID).first()
    user = User.query.filter_by(id=userID).first()
    user.lists.append(mlist)
    db.session.commit()

def remove_email_from_user(userID, emailID):
    user = User.query.filter_by(id=userID).first()
    email = Email.query.filter_by(id=emailID).first()
    user.emails.remove(email)
    db.session.commit()

def remove_list_from_user(userID, listID):
    mlist = MailingList.query.filter_by(id=listID).first()
    user = User.query.filter_by(id=userID).first()
    user.lists.remove(mlist)
    db.session.commit()