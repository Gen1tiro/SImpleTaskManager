from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()


def auth_check(login, password):
    if check_login(login) == 'login not found':
        return 'user not found'
    else:
        row = RegisteredUsers.query.filter(RegisteredUsers.login == login).all()
        if check_password_hash(row[0].psw, password):
            return 'user authorized'
        else:
            return 'wrong password'


def check_login(login):
    row = RegisteredUsers.query.filter(RegisteredUsers.login == login).all()
    if not row:
        return 'login not found'
    else:
        return 'login found'


class RegisteredUsers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(20), unique=True)
    psw = db.Column(db.String(500), nullable=False)
    codeword = db.Column(db.String(500))

    def __repr__(self):
        return f"<users {self.id}>"


class UsersMetaData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    surname = db.Column(db.String(30))
    role = db.Column(db.String(10))
    year_of_enter = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('registered_users.id'))

    def __repr__(self):
        return f"<users {self.id}>"


def add_new_user(login, psw, codeword, name, surname, role, year_of_enter):
    try:
        pass_hash = generate_password_hash(password=psw)
        codeword_hash = generate_password_hash(password=codeword)
        RU = RegisteredUsers(login=login, psw=pass_hash, codeword=codeword_hash)
        UMD = UsersMetaData(name=name, surname=surname, role=role, year_of_enter=year_of_enter, user_id=RU.id)
        db.session.add_all(UMD, RU)
        db.session.flush()
        db.session.commit()
        return 'user added'
    except Exception as e:
        db.session.rollback()
        print(e)
        return 'error'
