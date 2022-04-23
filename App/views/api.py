from flask import Blueprint, redirect, render_template, request, send_from_directory, flash

api_views = Blueprint('api_views', __name__, template_folder='../templates')

@api_views.route('/', methods=['GET'])
def get_api_docs():
    return render_template('index.html')

@api_views.route('/success', methods=['GET'])
def success():
    flash("Request successful")
    return render_template('index.html')

@api_views.route('/fail', methods=['GET'])
def fail():
    flash("Request unsuccessful")
    return render_template('index.html')
