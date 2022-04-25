from app import app
from flask import render_template, flash, redirect, url_for
from forms import LoginForm


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate():
        flash(f'Login requested for user {form.username.data}')
        return redirect(url_for('main_page'))
    return render_template('login.html', title='Login page', form=form)




