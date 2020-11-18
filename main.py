import sqlite3 as sql
from User import User

creating = '''
CREATE TABLE if NOT EXISTS users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name text not null,
age integer not null,
email text not null
);
'''


def create_db():
    connect = sql.connect('users.db')
    cur = connect.cursor()
    cur.execute(creating)


def connect_db():
    connect = sql.connect('users.db')
    # connect.row_factory = sql.Row
    return connect


def main():
    # wrapper = input(str('object: '))
    ob = User(connect_db())

    handlerName = input(str('name: '))
    ob.setName(handlerName)

    handlerAge = input(str('age: '))
    # print(type(handlerAge))
    ob.setAge(handlerAge)

    handlerEmail = input(str('email: '))
    ob.setEmail(handlerEmail)

    db = connect_db()
    db.cursor().execute('insert into users values (null, ?, ?, ?)', (ob.getName(), ob.getAge(), ob.getEmail()))
    db.commit()

if __name__ == '__main__':
    main()
