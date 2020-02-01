from hacksc2020 import app,db

if __name__ == "__main__":
    db.drop_all()
    db.create_all()
    #db.session.commit()

    from hacksc2020.models import User,Item
    user1 = User(username="boo",email="boo@yahoo.com",password="nmigga")
    item1 = Item(image="boo.jpg",name="name",price=4.20)
    item2 = Item(image="boo2.jpg",name="name2",price=2.40)

    db.session.add(item1)
    db.session.add(item2)
    db.session.add(user1)
    db.session.commit()
    print(User.query.all())
    print(Item.query.all())

    app.run(debug = True)
