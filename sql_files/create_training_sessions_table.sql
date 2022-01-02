CREATE TABLE IF NOT EXISTS training_sessions (
    id integer PRIMARY KEY autoincrement,
    duration float,
    performed_at date,
    location text,
    type integer,
    user_id integer,
    FOREIGN KEY(user_id) REFERENCES users(id)
);