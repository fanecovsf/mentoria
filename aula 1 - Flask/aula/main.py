from flask import Flask, jsonify
from models import db, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app=app)

@app.route('/')
def main():
    return 'Online'

@app.route('/users')
def users():
    users = db.session.query(User)

    users_list = []

    for user in users:
        data = {
            'id':user.id,
            'nome':user.nome,
            'idade':user.idade
        }

        users_list.append(data)

    return jsonify(users_list)
    

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()

        user1 = User(None, 'Henrique', 32)
        user2 = User(None, 'Gustavo', 23)

        user1.add()
        user2.add()

    app.run(debug=True, host='0.0.0.0')
