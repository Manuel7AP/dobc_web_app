from flask import render_template

from app import app
from app.models import Guest

@app.route('/guests', methods=['GET'])
def view_guests():
    return render_template('view_guests.html', guest_list=Guest.query.all())
