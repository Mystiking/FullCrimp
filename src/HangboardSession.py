import sqlite3
from typing import Optional
from datetime import date
from src.TrainingType import TrainingType
from src.TrainingSession import TrainingSession


class HangboardSession(TrainingSession):
    edge_size: int
    performed_at: date
    num_sets: int
    set_hang_time: int
    user_id: int
    training_session_id: int

    def __init__(self,
                 edge_size: int,
                 num_sets: int,
                 set_hang_time: int,
                 user_id: int,
                 performed_at: Optional[date] = date.today()):
        super().__init__(0.0, 'Home', TrainingType.HANGBOARD, user_id, performed_at)
        self.edge_size = edge_size
        self.num_sets = num_sets
        self.set_hang_time = set_hang_time
        self.user_id = user_id
        self.performed_at = performed_at

    def create(self):
        self.training_session_id = super().create()

        conn = sqlite3.connect('db/fullcrimp.db')
        c = conn.cursor()

        c.execute("""
                  INSERT INTO hangboard_sessions
                  (edge_size, num_sets, set_hang_time, parent_id) VALUES
                  ({0}, {1}, {2}, {3})
                  """.format(self.edge_size, self.num_sets, self.set_hang_time, self.training_session_id))

        conn.commit()


