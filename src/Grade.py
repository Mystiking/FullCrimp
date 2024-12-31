from enum import Enum


class GradeEnum(Enum):
    EASY = "4-"
    TRICKY_0 = "4"
    TRICKY_1 = "4+"
    DIFFICULT_0 = "5A"
    DIFFICULT_1 = "5B"
    HARD_0 = "5C"
    HARD_1 = "6A"
    HARD_2 = "6A+"
    VERY_HARD_0 = "6B"
    VERY_HARD_1 = "6B+"
    VERY_HARD_2 = "6C"
    VERY_HARD_3 = "6C+"
    EXTREME_0 = "7A"
    EXTREME_1 = "7A+"
    EXTREME_2 = "7B"
    EXTREME_3 = "7B+"
    EXTREME_4 = "7C"

    @staticmethod
    def map_to_range(grade):
        if grade == GradeEnum.EASY:
            return 'Easy'
        elif grade in [GradeEnum.TRICKY_0, GradeEnum.TRICKY_1]:
            return 'Tricky'
        elif grade in [GradeEnum.DIFFICULT_0, GradeEnum.DIFFICULT_1]:
            return 'Difficult'
        elif grade in [GradeEnum.HARD_0, GradeEnum.HARD_1, GradeEnum.HARD_2]:
            return 'Hard'
        elif grade in [GradeEnum.VERY_HARD_0, GradeEnum.VERY_HARD_1, GradeEnum.VERY_HARD_2, GradeEnum.VERY_HARD_3]:
            return 'Very Hard'
        elif grade in [GradeEnum.EXTREME_0, GradeEnum.EXTREME_1, GradeEnum.EXTREME_2, GradeEnum.EXTREME_3, GradeEnum.EXTREME_4]:
            return 'Extreme'
        else:
            return 'Elite'

    @staticmethod
    def get_route_enum_from_source(src):
        grade = src.split(".")[0]
        for g in GradeEnum:
            if grade == g.value:
                return g

        return GradeEnum.EASY

    @staticmethod
    def grade_comparison(a, b):
        # Assumed here is that a and b are strings from GradeEnum.value
        min_length = min(len(a), len(b))
        ac = a[:min_length]
        bc = b[:min_length]

        if ac > bc:
            return 1
        elif bc < ac:
            return -1
        else:
            if len(a) > len(b):
                return 1
            elif len(b) > len(a):
                return -1
            return 0

