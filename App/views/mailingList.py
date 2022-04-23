from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required


from App.controllers import (
    create_list, 
    add_recipient_to_list,
    remove_recipient_from_list,
    get_list,
    get_list_json,
    get_all_lists,
    get_all_lists_json,
    update_list,
    delete_list,
)

list_views = Blueprint('list_views', __name__, template_folder='../templates')

@list_views.route('/api/lists')
def get_lists_api():
    lists = get_all_lists_json()
    return jsonify(lists)

@list_views.route('/api/lists/<id>')
def get_list_api(id):
    return get_list_json(id)

@list_views.route('/lists')
def get_lists_page():
    lists = get_all_lists()
    return render_template('lists.html', lists=lists)

@list_views.route('/lists/<id>')
def get_list_page(id):
    list = get_list(id)
    return render_template('list.html', recipients=list.recipients)