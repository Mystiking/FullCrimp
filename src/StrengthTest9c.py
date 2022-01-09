class StrengthTest9c(object):
    points_to_grade = {
        1: '6a',
        2: '6a',
        3: '6b',
        4: '6b',
        5: '6c',
        6: '6c',
        7: '6c+',
        8: '6c+',
        9: '7a',
        10: '7a',
        11: '7a+',
        12: '7a+',
        13: '7b',
        14: '7b',
        15: '7b+',
        16: '7b+',
        17: '7c',
        18: '7c',
        19: '7c+',
        20: '7c+',
        21: '8a',
        22: '8a',
        23: '8a+',
        24: '8a+',
        25: '8b',
        26: '8b',
        27: '8b+',
        28: '8b+',
        29: '8c',
        30: '8c',
        31: '8c+',
        32: '8c+',
        33: '9a',
        34: '9a',
        35: '9a+',
        36: '9a+',
        37: '9b',
        38: '9b',
        39: '9b+',
        40: '9c',
    }

    core_exercise_map = {
        'L_sit_bend_knees': [10, 20, 30],
        'L_sit': [10, 15, 20],
        'Front_Lever': [5, 10, 20, 30]
    }

    def __init__(self):
        pass

    def calc_max_finger_strength_points(self, weight, added_weight):
        added_weight_ratio = added_weight / weight
        if added_weight_ratio < 0.1:
            return 1
        if added_weight_ratio < 0.2:
            return 2
        if added_weight_ratio < 0.3:
            return 3
        if added_weight_ratio < 0.4:
            return 4
        if added_weight_ratio < 0.5:
            return 5
        if added_weight_ratio < 0.6:
            return 6
        if added_weight_ratio < 0.8:
            return 7
        if added_weight_ratio < 1.0:
            return 8
        if added_weight_ratio < 1.2:
            return 9
        return 10

    def calc_max_pull_up_strength_points(self, weight, added_weight):
        added_weight_ratio = added_weight / weight
        if added_weight_ratio < 0.1:
            return 1
        if added_weight_ratio < 0.2:
            return 2
        if added_weight_ratio < 0.3:
            return 3
        if added_weight_ratio < 0.4:
            return 4
        if added_weight_ratio < 0.5:
            return 5
        if added_weight_ratio < 0.6:
            return 6
        if added_weight_ratio < 0.8:
            return 7
        if added_weight_ratio < 1.0:
            return 8
        if added_weight_ratio < 1.2:
            return 9
        return 10

    def calc_max_hang_points(self, duration):  # Duration in seconds
        if duration < 30:
            return 0
        if duration < 60:
            return 1
        if duration < 90:
            return 2
        if duration < 120:
            return 3
        if duration < 150:
            return 4
        if duration < 180:
            return 5
        if duration < 210:
            return 6
        if duration < 240:
            return 7
        if duration < 300:
            return 8
        if duration < 360:
            return 9
        return 10

    def calc_max_core_points(self, exercise, duration):
        points = 0
        if exercise == 'L_sit_bend_knees':
            for d in self.core_exercise_map[exercise]:
                if duration >= d:
                    points += 1
            return points
        points += 3
        if exercise == 'L_sit':
            for d in self.core_exercise_map[exercise]:
                if duration >= d:
                    points += 1
            return points
        points += 3
        if exercise == 'Front_Lever':
            for d in self.core_exercise_map[exercise]:
                if duration >= d:
                    points += 1
            return points
        return 0

    def convert_to_grade(self, points):
        return self.points_to_grade[points]
