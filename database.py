from sqlite3 import connect


def start_db():
    conn = connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS 'registered_users'(login TEXT, password TEXT, 
    name TEXT, surname TEXT, role TEXT, year_of_enter TEXT, codeword TEXT)""")
    conn.commit()


def add_new_user(login, password, name, surname, role, year, codeword):
    conn = connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO 'registered_users' VALUES (?, ?, ?, ?, ?, ?, ?)""",
                   (login, password, name, surname, role, year, codeword))
    conn.commit()


def login_check(login):
    conn = connect("database.db")
    cursor = conn.cursor()
    log = cursor.execute("""SELECT login FROM 'registered_users' WHERE login=?""", (login, ))
    if log.fetchone() is None:
        return 'ok'
    else:
        return 'login occupied'


def authorization(login, password):
    conn = connect("database.db")
    cursor = conn.cursor()
    if login_check(login) == 'ok':
        return 'user not found'
    else:
        cursor.execute(f"""SELECT password FROM 'registered_users' WHERE login = {login}""")
        row = cursor.fetchone()
        if row[0] == password:
            return 'user_authorized'
        else:
            return 'wrong_password'
