CREATE TABLE IF NOT EXISTS hangboard_sessions (
    id integer PRIMARY KEY autoincrement,
    edge_size int,
    num_sets int,
    set_hang_time int,
    parent_id integer,
    FOREIGN KEY(parent_id) REFERENCES training_sessions(id)
);