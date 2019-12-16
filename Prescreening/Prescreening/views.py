"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from Prescreening import app
from Prescreening.dlg_client import *
from flask import request, jsonify

@app.route('/')
@app.route('/home')
def home():
	init()
	return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
    
@app.route('/sendMessage', methods=["POST"])
def sendMessage():
    user_input = request.form.get('payload')
    system_data = process_message(user_input)
    return jsonify(system_data)