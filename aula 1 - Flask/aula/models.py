from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'tb_user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255))
    idade = db.Column(db.Integer)

    def __init__(self, id, nome, idade):
        self.id = id
        self.nome = nome
        self.idade = idade

    def add(self):
        db.session.add(self)
        db.session.commit()
