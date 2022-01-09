from typing import Optional, List
from datetime import date
import sqlite3
from src.TrainingType import TrainingType
from src.TrainingSession import TrainingSession
from src.ClimbingTypes import ClimbingType, ClimbingGym, BetaBouldersGrade


class ClimbingSession(TrainingSession):
    climbing_gym: ClimbingGym
    climbing_type: ClimbingType
    climbs: List[str]
    training_session_id: int

    def __init__(self,
                 duration: float,
                 location: str,
                 training_type: TrainingType,
                 user_id: int,
                 climbing_gym: ClimbingGym,
                 climbing_type: ClimbingType,
                 climbs: List[str],
                 performed_at: Optional[date] = date.today()):
        super().__init__(duration, location, training_type, user_id, performed_at)
        self.climbing_type = climbing_type
        self.climbing_gym = climbing_gym
        self.climbs = climbs

    def create(self):
        self.training_session_id = super().create()
        conn = sqlite3.connect('db/fullcrimp.db')
        c = conn.cursor()

        for climbing_grade in self.climbs:
            c.execute("""
            INSERT INTO climbing_sessions
            (climbing_gym, climbing_type, climbing_grade, parent_id) VALUES
            ({0}, {1}, '{2}', {3})
            """.format(self.climbing_gym.value, self.climbing_type.value, climbing_grade, self.training_session_id))

        conn.commit()
