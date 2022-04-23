from flask import Blueprint, redirect, url_for, render_template, jsonify, request, send_from_directory, flash
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
    get_all_lists,
)

email_views = Blueprint('email_views', __name__, template_folder='../templates')

@email_views.route('/api/emails')
def get_emails_api():
    emails = get_all_emails_json()
    return jsonify(emails)

@email_views.route('/api/emails/<id>')
def get_email_api(id):
    return get_email_json(id)

@email_views.route('/api/emails/send', methods=['POST'])
def send_email_api():
    data = request.get_json()
    if (data['id'] == "" or data['status'] == "sent"):
        id = create_email(data['list'], data['subject'], data['message'], "sent")
    else:
        update_email(data['id'], data['list'], data['subject'], data['message'], "sent")
        id = data['id']
    send_bulk(id)
    flash("Email sent")
    return render_template('index.html')

@email_views.route('/api/emails/update', methods=['UPDATE'])
def save_email_api():
    data = request.get_json()
    if (data['id'] == ""):
        id = create_email(data['list'], data['subject'], data['message'], "draft")
    else:
        print("log")
        update_email(data['id'], data['list'], data['subject'], data['message'], "draft")
    flash("Email saved")
    return render_template('index.html')

@email_views.route('/api/emails/delete/<id>', methods=['DELETE'])
def delete_email_api(id):
    delete_email(id)
    flash("Email deleted")
    return render_template('index.html')

@email_views.route('/emails/compose')
def get_compose_page():
    lists = get_all_lists()
    return render_template('compose.html', lists=lists)

@email_views.route('/emails/<id>')
def get_email_page(id):
    email = get_email(id)
    return render_template('email.html', email=email)

@email_views.route('/emails/sent')
def get_sent_page():
    emails = get_sent()
    return render_template('emails.html', emails=[emails, "Sent"])

@email_views.route('/emails/drafts')
def get_drafts_page():
    emails = get_drafts()
    return render_template('emails.html', emails=[emails, "Drafts"])

