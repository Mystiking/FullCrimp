import sqlite3
import os


if __name__ == '__main__':
    database = 'db/fullcrimp.db'
    conn = sqlite3.connect(database)

    c = conn.cursor()

    sql_files = [f for f in os.listdir('sql_files') if '.sql' in f]

    for sql_file in sql_files:
        with open('sql_files/' + sql_file, 'r') as fh:
            data = fh.read()
            c.execute(data)

    conn.commit()