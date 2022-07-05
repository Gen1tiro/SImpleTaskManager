from flask import Flask, request


from database import *


app = Flask(__name__)


@app.route('/reg', methods=['POST'])
def reg_solo_user():
    login = request.form['login']
    password = request.form['password']
    name = request.form['name']
    surname = request.form['surname']
    role = request.form['role']
    year_of_enter = request.form['year_of_enter']
    codeword = request.form['codeword']
    if login_check(login) == 'login occupied':
        return 'login_occupied'
    else:
        add_new_user(login, password, name, surname, role, year_of_enter, codeword)
    return 'user_added'


@app.route('/auth', methods=['POST'])
def auth():
    login = request.form['login']
    password = request.form['password']
    if authorization(login, password) == 'user not found':
        return 'user not found'
    elif authorization(login, password) == 'wrong_password':
        return 'wrong_password'
    else:
        return 'user_authorized'


if __name__ == '__main__':
    start_db()
    app.run(debug=True)
