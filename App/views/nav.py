from flask import Blueprint, redirect, render_template, request, send_from_directory


nav_views = Blueprint('api_navigation', __name__, template_folder='../templates/ExternalHTML')

@nav_views.route('/list', methods=['GET'])
def get_list_doc():
    return render_template('list.html')

@nav_views.route('/sent', methods=['GET'])
def get_sent_doc():
    return render_template('sent.html')

@nav_views.route('/draft', methods=['GET'])
def get_draft_doc():
    return render_template('draft.html')

@nav_views.route('/contact', methods=['GET'])
def get_contact_doc():
    return render_template('contact.html')

@nav_views.route('/account', methods=['GET'])
def get_account_doc():
    return render_template('account.html')

@nav_views.route('/compose', methods=['GET'])
def get_compose_doc():
    return render_template('compose.html')


