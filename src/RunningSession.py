from typing import Optional
from datetime import date
import sqlite3
from src.TrainingType import TrainingType
from src.TrainingSession import TrainingSession


class RunningSession(TrainingSession):
    distance: float
    training_session_id: int

    def __init__(self,
                 duration: float,
                 location: str,
                 training_type: TrainingType,
                 user_id: int,
                 distance: float,
                 performed_at: Optional[date] = date.today()):
        super().__init__(duration, location, training_type, user_id, performed_at)
        self.distance = distance

    def create(self):
        self.training_session_id = super().create()
        conn = sqlite3.connect('db/fullcrimp.db')
        c = conn.cursor()

        c.execute("""
        INSERT INTO running_sessions
        (distance, parent_id) VALUES
        ({0}, {1})
        """.format(self.distance, self.training_session_id))

        conn.commit()
