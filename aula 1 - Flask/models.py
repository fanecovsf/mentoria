from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'tb_users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    age = db.Column(db.Integer)

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age


class Order(db.Model):
    __tablename__ = 'tb_orders'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(255))

    def __init__(self, id, description):
        self.id = id
        self.description = description
    

