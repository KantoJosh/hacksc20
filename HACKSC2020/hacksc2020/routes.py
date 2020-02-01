from flask import Flask, escape, request,render_template,url_for,flash,redirect
from hacksc2020 import app,db
from hacksc2020.forms import RegistrationForm, LoginForm
from hacksc2020.models import User,Item

user = [
    {
        'username': 'Jigga',
        'email': 'sc@tidal.com',
        'password': 'password'
    },
    {
        'username': 'Ye',
        'email': 'kim@yeezy.com',
        'password': 'password'
    }
]
item = [
    {
        'image_file': '/static/apple.jpeg',
        'name': 'Apple',
        'price': 2.74 
    },
    {
        'image_file': '/static/apple.jpeg',
        'name': 'Apple',
        'price': 2.74 
    },
    {
        'image_file': '/static/apple.jpeg',
        'name': 'Apple',
        'price': 2.74 
    },
    {
        'image_file': '/static/apple.jpeg',
        'name': 'Apple',
        'price': 2.74 
    },
    {
        'image_file': '/static/pear.jpg',
        'name': 'Pear',
        'price': 3.99 
    },
    {
        'image_file': '/static/apple.jpeg',
        'name': 'Apple',
        'price': 2.74 
    },
    {
        'image_file': '/static/pear.jpg',
        'name': 'Pear',
        'price': 3.99 
    },
    {
        'image_file': '/static/apple.jpeg',
        'name': 'Apple',
        'price': 2.74 
    },
    {
        'image_file': '/static/pear.jpg',
        'name': 'Pear',
        'price': 3.99 
    }
]

@app.route('/',methods =["GET","POST"])
@app.route('/home',methods =["GET","POST"])
def home():
    return render_template("home.html",title="Home", item=item)

@app.route('/register',methods =["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        print(User.query.all())
        return redirect(url_for("login"))
    return render_template("register.html",title="Register",form=form)


@app.route('/login',methods =["GET","POST"])
def login():
    form = LoginForm()  
    return render_template("login.html",title="Login",form=form)

@app.route('/cart',methods =["GET","POST"])
def cart():
    return render_template("cart.html",title="Cart")