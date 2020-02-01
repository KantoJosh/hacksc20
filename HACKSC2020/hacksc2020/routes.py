from flask import Flask, escape, request,render_template,url_for,flash,redirect
from hacksc2020 import app,db
from hacksc2020.forms import RegistrationForm, LoginForm

@app.route('/',methods =["GET","POST"])
def home():
    return render_template("home.html",title="Home")

@app.route('/register',methods =["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for("home"))
    return render_template("register.html",title="Register",form=form)


@app.route('/login',methods =["GET","POST"])
def login():
    form = RegistrationForm()  
    return render_template("login.html",title="Login",form=form)