import sqlite3
from typing import Optional
from datetime import date


class Weight(object):
    weight: float
    weighed_at: date
    user_id: int

    def __init__(self,
                 weight: float,
                 user_id: int,
                 weighed_at: Optional[date] = date.today()):
        self.weight = weight
        self.user_id = user_id
        self.weighed_at = weighed_at

    def create(self):
        conn = sqlite3.connect('db/fullcrimp.db')
        c = conn.cursor()

        c.execute("""
        INSERT INTO weight
        (weight, weighed_at, user_id) VALUES
        ({0}, '{1}', {2})
        """.format(self.weight, self.weighed_at, self.user_id))

        conn.commit()

        return c.lastrowid

    @staticmethod
    def get_latest_weight(user_id):
        conn = sqlite3.connect('db/fullcrimp.db')
        c = conn.cursor()

        c.execute("""
        SELECT * FROM weight
        WHERE user_id = {0}
        ORDER BY weighed_at DESC;
        """.format(user_id))

        most_recent_weight = c.fetchone()

        if most_recent_weight is None:
            return None

        return most_recent_weight[1]
