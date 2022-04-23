from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash
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
    get_all_recipients,
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
    return render_template('list.html', list=list)

@list_views.route('/api/lists/create', methods=['POST'])
def create_list_api():
    data = request.get_json()
    if (data[0]['id'] == ""):
        id = create_list(data[0]['name'])
        for recip in data[1]:
            add_recipient_to_list(id, recip)
        flash("List created")
    else:
        update_list(data[0]['id'], data[0]['name'])
        flash("List updated")
    return render_template('index.html')

@list_views.route('/api/lists/delete/<id>', methods=['DELETE'])
def delete_list_api(id):
    delete_list(id)
    flash("List deleted")
    return render_template('index.html')

@list_views.route('/lists/create')
def get_create_page():
    recips = get_all_recipients()
    return render_template('createList.html', recips=recips)