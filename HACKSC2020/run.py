from hacksc2020 import app,db

if __name__ == "__main__":
    db.drop_all()
    db.create_all()
    #db.session.commit()

    from hacksc2020.models import User,Item
    item1 = Item(image="boo.jpg",name="name",price=4.20)
    item2 = Item(image="boo2.jpg",name="name2",price=2.40)

    __USER__ = User(username = "USER",email="user@hacksc.com",password="hacksc")
    db.session.add(__USER__)
    db.session.commit()
    print(User.query.all())
    print(Item.query.all())

    app.run(debug = True)
