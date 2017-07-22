from flask import flash, redirect, render_template, url_for, request
from sqlalchemy.exc import IntegrityError

from app import app, db
from app.forms import AddGuestForm
from app.models import Guest
from app.util import flash_form_errors


@app.route('/guests/create', methods=['GET', 'POST'])
def add_guest():
    add_guest_form = AddGuestForm()
    if request.method == 'GET':
        return render_template('add_guest.html', add_guest_form=add_guest_form)
    if request.method == 'POST':
        guest = Guest(add_guest_form.name.data, add_guest_form.message.data)
        db.session.add(guest)
        db.session.commit()
        return redirect(url_for('view_guests'))
