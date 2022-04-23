from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required


from App.controllers import (
    create_recipient, 
    create_recipients_from_csv,
    get_recipient,
    get_recipient_json,
    get_all_recipients,
    get_all_emails,
    get_all_recipients_json,
    update_recipient,
    delete_recipient,
)

recipient_views = Blueprint('recipient_views', __name__, template_folder='../templates')


@recipient_views.route('/api/recipients')
def get_recipients_api():
    recipients = get_all_recipients_json()
    return jsonify(recipients)

@recipient_views.route('/api/recipients/<id>')
def get_recipient_api(id):
    return get_recipient_json(id)

@recipient_views.route('/recipients')
def get_recipients_page():
    recips = get_all_recipients()
    return render_template('recipients.html', recips=recips)