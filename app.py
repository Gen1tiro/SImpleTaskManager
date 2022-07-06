from flask import Flask, request

from database import *
from database import check_login

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)


def get_login_password():
    login = request.form['login']
    password = request.form['psw']
    return login, password


@app.route('/reg', methods=['POST'])
def reg_solo_user():
    login, password = get_login_password()
    name = request.form['name']
    surname = request.form['surname']
    role = request.form['role']
    year_of_enter = request.form['year_of_enter']
    codeword = request.form['codeword']
    if check_login(login) != 'login not found':
        return 'login occupied'
    else:
        if add_new_user(login, password, codeword, name, surname, role, year_of_enter) == 'user added':
            return 'user added'
        else:
            return 'error'


@app.route('/auth', methods=['POST'])
def auth():
    login, password = get_login_password()
    return auth_check(login, password)


if __name__ == '__main__':
    app.run(debug=True)
