from distutils.command.config import config
import json
from flask import Flask, Blueprint, redirect, render_template, request, send_from_directory, url_for, flash, jsonify, session, make_response
from flask_login import current_user
from App.controllers import auth
import jwt
from datetime import datetime, timedelta
from functools import wraps
import os
from flask_uploads import DOCUMENTS, IMAGES, TEXT, UploadSet, configure_uploads
from flask_cors import CORS
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from App.controllers.auth import authenticate, login_user

api_views = Blueprint('api_views', __name__, template_folder='../templates')


@api_views.route('/', methods=['GET'])
def get_api_docs():
    return render_template('homepage.html')

@api_views.route('/success', methods=['GET'])
def success():
    flash("Request successful")
    return render_template('index.html')

@api_views.route('/fail', methods=['GET'])
def fail():
    flash("Request unsuccessful")
    return render_template('index.html')







