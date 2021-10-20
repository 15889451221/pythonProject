import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def test_sqlalchemy():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://tmp_hello:asdzxc123456@106.52.42.50/tmp123?charset=utf8mb4"
    db = SQLAlchemy(app)


    class user(db.Model):
        #__tablename__ = "xxx"
        id = db.Column(db.Integer,primary_key=True)
        username = db.Column(db.String(80),unique=True,nullable=False)
        email = db.Column(db.String(120),unique=True,nullable=False)

        def __repr__(self):
            return '<User %r>' %self.username
    #db.create_all()
    db.session.add(user(id="2",username="xiaolv",email="abc@163.com"))
    db.session.commit()



