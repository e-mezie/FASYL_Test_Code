from flask import Flask, render_template, url_for, flash, redirect
from main import app, db
from main.forms import RegistrationForm, LoginForm
from main.modules import User


@app.route ('/home')
def home():
    return render_template ('home.html')


@app.route ('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm ()
    if form.validate_on_submit ():
        user = User(firstname=form.firstname.data, lastname=form.lastname.data, email_address=form.email.data, reference_code=form.reference_code.data)
        db.create_all()
        db.session.add(user)
        db.session.commit()
        flash (f'Account Created for {form.firstname.data}!', 'success')
        return redirect (url_for ('login'))
    return render_template ('registration.html', title='Registration', form=form)


@app.route ('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm ()
    if form.validate_on_submit ():
        if form.email.data == RegistrationForm:
            flash ('You have been logged in!', 'success')
            return redirect (url_for ('home'))
        else:
            flash ('Login Unsuccessful, Please check username and password', 'danger')
    return render_template ('login.html', title='Login', form=form)