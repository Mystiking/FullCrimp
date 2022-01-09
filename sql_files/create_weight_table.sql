CREATE TABLE IF NOT EXISTS weight (
    id integer PRIMARY KEY autoincrement,
    weight float,
    weighed_at date,
    user_id integer,
    FOREIGN KEY(user_id) REFERENCES users(id)
);