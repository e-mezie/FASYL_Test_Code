from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask (__name__)

app.config['SECRET_KEY'] = 'cfe396b1a27c2914da6b7e45dee37180'


@app.route ('/home')
def home():
    return render_template ('home.html')


@app.route ('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template ('registration.html', title='Registration', form=form)


@app.route ('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit ():
        if form.email.data == 'nweke@gmail.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful, Please check username and password', 'danger')
    return render_template ('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run (debug=True)
