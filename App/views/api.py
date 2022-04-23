<<<<<<< HEAD
from flask import Blueprint, redirect, render_template, request, send_from_directory, url_for
from flask_login import current_user
from App.controllers import auth

from App.controllers.auth import authenticate, login_user

=======
from flask import Blueprint, redirect, render_template, request, send_from_directory, flash
>>>>>>> 432424be47fffc56de1e07913110811ff7f5704a

api_views = Blueprint('api_views', __name__, template_folder='../templates')

@api_views.route('/', methods=['GET'])
def get_api_docs():
    return render_template('homepage.html')

@api_views.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form["user"]
        passw = request.form["passkey"]
        check = request.form.getlist("remember-me")

        current_user = authenticate(user, passw)
        if(current_user != None):
            # login_user(current_user, remember = True)
            return redirect(url_for('api_views.get_layout_docs', usr = user))  
    else:
        return render_template('homepage.html')


@api_views.route('/home/<usr>', methods=['GET'])
def get_layout_docs(usr):
        return render_template('layout.html')   




