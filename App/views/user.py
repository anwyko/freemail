from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required


from App.controllers import (
    create_user, 
    get_user,
    get_user_json,
    get_all_users,
    get_all_users_json,
    update_user,
    change_password,
    delete_user,
    add_email_to_user,
    add_list_to_user,
    remove_email_from_user,
    remove_list_from_user,
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')


@user_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users)

@user_views.route('/static/users')
def static_user_page():
  return send_from_directory('static', 'static-user.html')

@user_views.route('/api/users', methods=['GET'])
def get_users_api():
    users = get_all_users_json()
    return jsonify(users)

@user_views.route('/api/users/<id>')
def get_user_api(id):
    return get_user_json(id)