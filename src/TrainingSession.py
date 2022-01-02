import sqlite3
from typing import Optional
from datetime import date
from src.TrainingType import TrainingType


class TrainingSession(object):
    duration: float
    performed_at: date
    location: str
    training_type: TrainingType
    user_id: int

    def __init__(self,
                 duration: float,
                 location: str,
                 training_type: TrainingType,
                 user_id: int,
                 performed_at: Optional[date] = date.today()):
        self.duration = duration
        self.location = location
        self.training_type = training_type
        self.user_id = user_id
        self.performed_at = performed_at

    def create(self):
        conn = sqlite3.connect('db/fullcrimp.db')
        c = conn.cursor()

        c.execute("""
        INSERT INTO training_sessions
        (duration, performed_at, location, type, user_id) VALUES
        ({0}, '{1}', '{2}', '{3}', {4})
        """.format(self.duration, self.performed_at, self.location, self.training_type.value, self.user_id))

        conn.commit()

        return c.lastrowid


