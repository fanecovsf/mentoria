from flask import Flask, render_template, request, redirect, url_for, jsonify
from models import db, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app=app)

@app.route('/')
def index():
    return 'Online'

@app.route('/users')
def users():
    users = db.session.query(User).all()

    data_list = []

    for user in users:
        data = {
            'id':user.id,
            'name':user.name,
            'age':user.age
        }

        data_list.append(data)

    return jsonify(data_list)
    

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()

        user1 = User(None, 'Gustavo', 23)
        user2 = User(None, 'Luciano', 32)

        db.session.add_all([user1, user2])

        db.session.commit()

    app.run(debug=True)
