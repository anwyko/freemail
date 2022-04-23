from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required


from App.controllers import (
    create_email, 
    add_list_to_email,
    remove_list_from_email,
    send_email,
    send_bulk,
    get_email,
    get_sent,
    get_drafts,
    get_email_json,
    get_all_emails,
    get_all_emails_json,
    update_email,
    delete_email,
)

email_views = Blueprint('email_views', __name__, template_folder='../templates')

@email_views.route('/api/emails')
def get_emails_api():
    emails = get_all_emails_json()
    return jsonify(emails)

@email_views.route('/api/emails/<id>')
def get_email_api(id):
    return get_email_json(id)

@email_views.route('/emails/sent')
def get_sent_page():
    emails = get_sent()
    return render_template('sent.html', emails=emails)

@email_views.route('/emails/drafts')
def get_drafts_page():
    emails = get_drafts()
    return render_template('drafts.html', emails=emails)

@email_views.route('/emails/<id>')
def get_email_page(id):
    email = get_email(id)
    return render_template('email.html', email=email)