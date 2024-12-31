CREATE TABLE IF NOT EXISTS routes (
    id integer PRIMARY KEY autoincrement,
    set_at date,
    setter text,
    grade text,
    hold_color text,
    pos_x float,
    pos_y float
);