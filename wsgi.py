import click
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import create_db
from App.main import app, migrate, populate_db
from App.controllers import *

# This commands file allow you to create convenient CLI commands
# for testing controllers

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def initialize():
    create_db(app)
    print('database intialized')

@app.cli.command("pop", help="Populates the database")
def populate():
    populate_db()
    print('database populated')

'''
USER COMMANDS
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

@user_cli.command("add-email", help="Adds an email to a user")
def add_email_command():
    add_email_to_user()

@user_cli.command("add-list", help="Adds an list to a user")
def add_list_command():
    add_list_to_user()

app.cli.add_command(user_cli) # add the group to the cli




'''
Email Commands
'''
email_cli = AppGroup('email', help='User object commands') 

@email_cli.command("create", help="Creates an email")
@click.argument("subject", default="subject")
@click.argument("body", default="body")
@click.argument("status", default="draft")
def create_email_command(subject, body, status):
    create_email(subject, body, status)
    print(f'email created!')

@email_cli.command("send", help="ASends an email")
def send_command():
    send_email()

@email_cli.command("send-bulk", help="ASends an email")
def send_bulk_command():
    send_bulk(2)

@email_cli.command("add-list", help="Adds a recipient to a list")
def add_list_command():
    add_list_to_email()
    # print(f'recip added!')

app.cli.add_command(email_cli)




'''
RECIPIENT COMMANDS
'''
recip_cli = AppGroup('recip', help='User object commands') 

@recip_cli.command("create", help="Creates a recipient")
@click.argument("firstname", default="jane")
@click.argument("lastname", default="doe")
@click.argument("email", default="email")
def create_recipient_command(firstname, lastname, email):
    create_recipient(firstname, lastname, email)
    print(f'recipient created!')

app.cli.add_command(recip_cli)




'''
MAILINGLIST COMMANDS
'''
list_cli = AppGroup('list', help='User object commands') 

@list_cli.command("create", help="Creates a list")
@click.argument("name", default="list")
def create_list_command(name):
    create_list(name)
    print(f'list created!')

@list_cli.command("add-recip", help="Adds a recipient to a list")
def add_list_command():
    add_recipient_to_list(2, 7)
    # print(f'recip added!')

@list_cli.command("rem-recip", help="Adds a recipient to a list")
def add_list_command():
    remove_recipient_from_list(2, 3)
    # print(f'recip added!')

app.cli.add_command(list_cli)




'''
Generic Commands
'''
@app.cli.command("init")
def initialize():
    create_db(app)
    print('database intialized')

