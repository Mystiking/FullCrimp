import sqlite3
from typing import Optional


class User(object):
    id: int
    name: str
    username: str

    class UsernameOrPasswordWrong(Exception):
        pass

    def __init__(self, id: int, name: str, username: str):
        self.id = id
        self.name = name
        self.username = username

    @staticmethod
    def get_user(username: str, password: str):
        conn = sqlite3.connect('db/fullcrimp.db')
        c = conn.cursor()
        c.execute("""
            SELECT * FROM users
                WHERE username = '{0}'
                AND password = '{1}';
        """.format(username, password))
        user = c.fetchone()
        if user is None:
            raise User.UsernameOrPasswordWrong("Username or password is wrong.")

        return User(user[0], user[1], user[2])

    @staticmethod
    def create_user(username: str, password: str, name: Optional[str] = ""):
        conn = sqlite3.connect('db/fullcrimp.db')
        c = conn.cursor()
        c.execute("""
        SELECT * FROM users WHERE username = '{0}';
        """.format(username))

        usernames = c.fetchone()
        if len(usernames) > 0:
            raise Exception("Username already in use.")

        c.execute("""
        INSERT INTO users (name, username, password)
        VALUES ('{0}', '{1}', '{2}');
        """.format(name, username, password))

        conn.commit()

        return User.get_user(username, password)
