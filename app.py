"""Quick Flask App - routes & app factory"""
import os
import requests
from functools import wraps
from flask import Flask, request, render_template, jsonify, redirect, url_for, flash, session
from flask_cors import CORS
from flask_session import Session

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = "secret"
CORS(app)  # Enable CORS for all routes and origins (safe for internal APIs)
Session(app)

# Assign per-route to link specific apps to associated frontend features
app_id = os.environ.get("app_id")
owner_id = os.environ.get("owner_id")


def signin_required(view_func):
    """
    Define route check
    :param view_func:
    :return:
    """
    @wraps(view_func)
    def wrapped_view(*args, **kwargs):
        """
        Route check logic
        :param args:
        :param kwargs:
        :return:
        """
        if not session.get("user"):
            flash("Please sign in to continue.", "warning")
            return redirect(url_for("index"))
        return view_func(*args, **kwargs)
    return wrapped_view


@app.route('/')
def index():
    """

    :return:
    """
    if session.get("signed_in"):
        flash("Please sign out first.", "warning")
        return redirect(url_for('portal'))
    return render_template('index.html')


@app.route('/signin', methods=["POST"])
def signin():
    """
    For demo purposes only. Proper authentication should be used.
    :return:
    """
    email = request.form.get("email")
    password = request.form.get("pwd")  # to be used in production authentication
    print(f"Email: {email}")
    res = requests.post("https://www.natrul.ai/api/v1/apps/users", json={
        "app_id": app_id,
        "owner_id": owner_id
    })

    parsed = res.json()

    # Extract the users list
    users = parsed.get("data", {}).get("users", [])
    valid_user = None
    for user in users:
        if email == user["email"]:
            valid_user = user

    if valid_user:
        session["user"] = valid_user
        flash("Sign-in successful!", "success")
        return redirect(url_for('portal'))
    else:
        flash("Incorrect email or password.", "danger")
        return redirect(url_for('index'))

@app.route('/portal', methods=["GET"])
@signin_required
def portal():
    """
    Contains frontend for AI features
    - APIs fetched from javascript
    :return:
    """
    user = session.get("user")
    return render_template('portal.html', user=user, app_id=app_id)


@app.route('/dashboard', methods=["GET"])
@signin_required
def dashboard():
    """
    Contains frontend for AI features
    - APIs fetched from javascript
    :return:
    """
    user = session.get("user")
    return render_template('dashboard.html', user=user, app_id=app_id)


@app.route('/email-generator', methods=["GET"])
@signin_required
def email_gen():
    """
    Contains frontend for AI features
    - APIs fetched from javascript
    :return:
    """
    user = session.get("user")
    return render_template('email_generator.html', user=user, app_id=app_id)


@app.route('/policy-explainer', methods=["GET"])
@signin_required
def policy_explainer():
    """
    Contains frontend for AI features
    - APIs fetched from javascript
    :return:
    """
    user = session.get("user")
    return render_template('policy_explainer.html', user=user, app_id=app_id)


@app.route('/tech-doc-finderr', methods=["GET"])
@signin_required
def tech_doc_finder():
    """
    Contains frontend for AI features
    - APIs fetched from javascript
    :return:
    """
    user = session.get("user")
    return render_template('tech_doc_finder.html', user=user, app_id=app_id)


@app.route('/sign-out', methods=["GET"])
def signout():
    """

    :return:
    """
    if session.get("user"):
        session.clear()
        flash("You've been signed out.", "primary")
    else:
        flash("You're not signed in.", "warning")
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
