from flask import Blueprint, render_template, redirect, url_for, session


main = Blueprint('main', __name__)
auth = Blueprint('auth', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route("/signup")
def signup():
    return render_template("signup.html")

@main.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@auth.route('/logout')
def logout():
    session.clear()  # Optional: clear session/login data
    return redirect(url_for('main.home'))  # Redirects to "/"

@main.route('/report', methods=['GET', 'POST'])
def report():
    return render_template('report.html')
