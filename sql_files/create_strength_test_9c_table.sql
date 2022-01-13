CREATE TABLE IF NOT EXISTS strength_test_9c (
    id integer PRIMARY KEY autoincrement,
    performed_at date,
    weight float,
    core_level text,
    core_time float,
    pull_up_weight float,
    hang_time float,
    hang_board_weight float,
    grade text,
    points int,
    user_id integer,
    FOREIGN KEY(user_id) REFERENCES users(id)
);