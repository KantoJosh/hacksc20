from flask import Flask, escape, request,render_template,url_for,flash,redirect
from hacksc2020 import app,db
from hacksc2020.forms import RegistrationForm, LoginForm

@app.route('/',methods =["GET","POST"])
def home():
    return render_template("layout.html",title="Home")

@app.route('/register',methods =["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password)
        db.session.add(user)
        db.commit()
        return redirect(url_for("login"))
    return render_template("register.html",title="Register",form=form)


@app.route('/login',methods =["GET","POST"])
def login():
    form = LoginForm()  
    return render_template("login.html",title="Login",form=form)