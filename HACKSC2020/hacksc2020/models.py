from hacksc2020 import db

class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(30), unique = True, nullable = False)
    email = db.Column(db.String(30), unique = True, nullable = False)
    password = db.Column(db.String(100),nullable=False)
    cart = db.Column(db.String(100),default="")

    def __repr__(self):
        return f"Username={self.username},email={self.email}"
    
    def add_to_cart(self,id_name):
        print("BEFORE")
        self.cart += f"{id_name}/"
        db.session.commit()
        print("ADDED:",self.cart)
    


class Item(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    image = db.Column(db.String(30),unique=False,nullable = False)
    name = db.Column(db.String(100),unique=False,nullable=False)
    price = db.Column(db.Float)
    stock = db.Column(db.Integer,default = 10)

    def __repr__(self):
        return f"Item:image = {self.image}, name = {self.name}, price = {self.price}"
