CREATE TABLE IF NOT EXISTS running_sessions (
    id integer PRIMARY KEY autoincrement,
    distance float,
    parent_id integer,
    FOREIGN KEY(parent_id) REFERENCES training_sessions(id)
);