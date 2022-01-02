CREATE TABLE IF NOT EXISTS users (
    id integer PRIMARY KEY autoincrement,
    name text,
    username text NOT NULL,
    password text NOT NULL
);