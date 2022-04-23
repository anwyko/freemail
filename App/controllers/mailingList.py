from App.models import Email, User, MailingList, Recipient
from App.database import db


def create_list(name):
    mlist = MailingList(name=name)
    db.session.add(mlist)
    db.session.commit()
    return mlist.id

def add_recipient_to_list(listID, recipientID):
    mlist = MailingList.query.filter_by(id=listID).first()
    recipient = Recipient.query.filter_by(id=recipientID).first()
    mlist.recipients.append(recipient)
    db.session.commit()

def remove_recipient_from_list(listID, recipientID):
    mlist = MailingList.query.filter_by(id=listID).first()
    recipient = Recipient.query.filter_by(id=recipientID).first()
    mlist.recipients.remove(recipient)
    db.session.commit()

def get_all_lists():
    return MailingList.query.all()

def get_list(listID):
    return MailingList.query.filter_by(id=listID).first()

def get_all_lists_json():
    lists = MailingList.query.all()
    if not lists:
        return []
    lists = [mlist.toDict() for mlist in lists]
    return lists

def get_list_json(listID):
    mlist = MailingList.query.filter_by(id=listID).first()
    if not mlist:
        return False
    return mlist.toDict()

def delete_list(listID):
    mlist = MailingList.query.filter_by(id=listID).first()
    if mlist == None:
        return False
    db.session.delete(mlist)
    db.session.commit()
    return True

def update_list(listID, name):
    mlist = MailingList.query.filter_by(id=listID).first()
    if mlist == None:
        return False
    mlist.name = name
    db.session.add(mlist)
    db.session.commit()
    return True
