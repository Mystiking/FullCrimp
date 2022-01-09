CREATE TABLE IF NOT EXISTS climbing_sessions (
    id integer PRIMARY KEY autoincrement,
    climbing_gym int,
    climbing_type int,
    climbing_grade text,
    parent_id integer,
    FOREIGN KEY(parent_id) REFERENCES training_sessions(id)
);