from typing import Optional
from datetime import date
from src.TrainingType import TrainingType
from src.TrainingSession import TrainingSession


class YogaSession(TrainingSession):
    def __init__(self,
                 duration: float,
                 location: str,
                 training_type: TrainingType,
                 user_id: int,
                 performed_at: Optional[date] = date.today()):
        super().__init__(duration, location, training_type, user_id, performed_at)

    def create(self):
        super().create()
