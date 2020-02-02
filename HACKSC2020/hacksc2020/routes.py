import os
from flask import Flask, escape, request,render_template,url_for,flash,redirect,jsonify
from hacksc2020 import app, db
# from flask_login import login_user, current_user, logout_user, login_required
from hacksc2020.forms import RegistrationForm, LoginForm,DropdownForm
from hacksc2020.models import User,Item
# import stripe

# stripe_keys = {
#   'secret_key': os.environ['STRIPE_SECRET_KEY'],
#   'publishable_key': os.environ['STRIPE_PUBLISHABLE_KEY']
# }

# stripe.api_key = stripe_keys['secret_key']


itemList = [
    Item(image='/static/apple1.jpg',name='apple',price=0.25),
    Item(image='/static/pear13.jpg',name='pear',price=0.51 ),
    Item(image='/static/banana3.jpg',name='banana',price=0.15),
    Item(image='/static/carrot2.jpg',name='carrot',price=0.14),
    Item(image='/static/orange1.jpg',name='orange',price=0.42),
    Item(image='/static/grapes1.jpg',name='grapes',price=2.35),
]

@app.route('/',methods =["GET","POST"])
@app.route('/home',methods =["GET","POST"])
def home():
    for it in itemList:
        db.session.add(it)
    db.session.commit()
    return render_template("home.html",title="Home", item=itemList)

@app.route('/register',methods =["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html",title="Register",form=form)


@app.route('/login',methods =["GET","POST"])
def login():
    form = LoginForm()  
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
    return render_template("home.html",title="Login",form=form)


# @app.route('/<itemid>',methods=["GET","POST"])
# def product_page(file):
#     return render_template(file)
#     # mapping of object name ('orange':file)




# click on image: href is a url_for to product_page
@app.route('/cart/<id>',methods =["GET","POST"])
def cart(id):
    # form = DropdownForm()
    # print("QUANTITY: ",form.quantity.data)
    print(id)
    user = User.query.filter_by(username="USER").first()
    user.add_to_cart(id)
    #return render_template("cart.html",title="Cart",items=items)
    our_cart = []
    total_price = 0
    for item in user.cart.rstrip("  \n").split("/"):
        if len(item) > 0:
            our_cart.append(Item.query.filter_by(id=int(item)).first()) # each item is an Item object
            total_price += Item.query.filter_by(id=int(item)).first().price

    return render_template("cart.html",title="Cart",items=our_cart,total_price=total_price)

@app.route('/pay',methods =["GET","POST"])
def pay():
    return render_template("pay.html",title="Pay", key=stripe_keys['publishable_key'])


#background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    print ("Hello")
    return ("nothing")