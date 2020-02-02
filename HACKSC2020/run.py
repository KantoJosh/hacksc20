from hacksc2020 import app,db

if __name__ == "__main__":
    db.drop_all()
    db.create_all()
    #db.session.commit()

    from hacksc2020.models import User,Item

    __USER__ = User(username = "USER",email="user@hacksc.com",password="hacksc")
    db.session.add(__USER__)
    db.session.commit()
    print("USERS: ",User.query.all())

    app.run(debug = True)
