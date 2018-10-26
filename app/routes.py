from app import app
from flask import render_template, redirect, make_response, request, flash
from app.forms import LoginForm, RegistrationForm, NewPasswdForm

users = {"root": "12345"}

@app.route('/')
@app.route("/index")
def index():
    username = request.cookies.get("username")
    if not username:
        username = "guest"
    return render_template("index.html", username=username)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.cookies.get("logged_in"):
        flash("Already logged in!")
        return redirect("/index")
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        passwd = form.passwd.data
        if (username in users) and users[username] == passwd:
            resp = make_response(redirect("/index"))
            resp.set_cookie("username", username)
            resp.set_cookie("logged_in", "1")
            flash("Logged in successfully.")
            return resp
        if not username in users:
            flash("Failed to log in. No such username.")
        else:
            flash("Failed to log in. Incorrect password.")
    return render_template("login.html", form=form)

@app.route("/reg", methods=["GET", "POST"])
def reg():
    if request.cookies.get("logged_in"):
        flash("Already logged in! Log out, then register.")
        return redirect("/index")
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        passwd = form.passwd.data
        retpasswd = form.retpasswd.data
        if username in users:
            flash("This username already used. Try with another one.")
            return render_template("reg.html", form=form)
        if passwd == retpasswd:
            users[username] = passwd
            flash("Registrated successfully.")
            return redirect("/index")
        flash("Passwords didn't match. Please, try again.")
    return render_template("reg.html", form=form)

@app.route("/newpasswd", methods=["GET", "POST"])
def newpasswd():
    if not request.cookies.get("logged_in"):
        flash("Log in first.")
        return redirect("/login")
    form = NewPasswdForm()
    if form.validate_on_submit():
        oldpasswd = form.oldpasswd.data
        newpasswd = form.newpasswd.data
        retpasswd = form.retpasswd.data
        username = request.cookies.get("username")
        if users[username] != oldpasswd:
            flash("Old password incorrect.")
            return render_template("newpasswd.html", form=form)
        if newpasswd != retpasswd:
            flash("New passwords didn't match. Please, try again.")
            return render_template("newpasswd.html", form=form)
        users[username] = newpasswd
        flash("Password changed successfully.")
        return redirect("/index")
    return render_template("newpasswd.html", form=form)

@app.route("/logout")
def logout():
    resp = make_response(redirect("/index"))
    if not request.cookies.get("logged_in"):
        flash("Already logged out!")
        return redirect("/index")
    resp.set_cookie("username", "guest")
    resp.set_cookie("logged_in", "")
    flash("Logged out successfully.")
    return resp

