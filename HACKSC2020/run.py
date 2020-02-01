from hacksc2020 import app,db

if __name__ == "__main__":
    db.drop_all()
    db.create_all()
    # db.session.commit()
    app.run(debug = True)
