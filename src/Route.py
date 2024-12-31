from src.Grade import GradeEnum
import numpy as np
import cv2
import sqlite3
from typing import List
from datetime import date, datetime
import math


class Route(object):
    route_thumbnails: str = "assets/grades/"
    id: int = -1
    setter: str = ""
    date_set: str = ""
    pos: List[float] = [0, 0]
    grade: GradeEnum = None
    hold_color: str = "white"
    img: None

    def __init__(self, grade_enum: GradeEnum, pos: List[float], setter: str = "", set_date: str = date.today().strftime('%Y/%m/%d'), hold_color: str = "white", id: int = -1):
        self.grade = grade_enum
        self.pos = pos
        self.setter = setter
        self.date_set = set_date
        self.hold_color = hold_color
        self.id = id

        self.update_thumbnail_with_route_color()

        self.x_offset = int(max(pos[0] - self.img.shape[1] / 2, 0))
        self.y_offset = int(max(pos[1] - self.img.shape[0] / 2, 0))

        self.min = [self.y_offset, self.x_offset]
        self.max = [self.y_offset + self.img.shape[0], self.x_offset + self.img.shape[1]]

    def update_thumbnail_with_route_color(self):
        hold_pixel_color = cv2.imread("assets/gym/hold_colors/" + self.hold_color + ".png")[3:-3, 3:-3][0, 0]
        if np.sum(hold_pixel_color) == 0:
            hold_pixel_color = [3, 3, 3]
        self.img = cv2.imread(self.route_thumbnails + self.grade.value + ".png")
        img_center = [self.img.shape[0] / 2, self.img.shape[1] / 2]
        radius = 20
        for i in range(self.img.shape[0]):
            for j in range(self.img.shape[1]):
                if math.dist([j, i], img_center) > radius:
                    if np.sum(self.img[j, i]) != 0:
                        self.img[j, i] = hold_pixel_color

    def set_setter(self, setter):
        self.setter = setter

    def set_id(self, id):
        self.id = id

    def is_point_inside(self, pos):
        return self.min[0] <= pos[1] <= self.max[0] and self.min[1] <= pos[0] <= self.max[1]

    def add_route_to_db(self):
        success, d = Route.validate_date(self.date_set)
        if not success:
            return False

        conn = sqlite3.connect('db/fullcrimp.db')
        c = conn.cursor()
        c.execute("""
                INSERT INTO routes (set_at, setter, grade, hold_color, pos_x, pos_y)
                VALUES ('{0}', '{1}', '{2}', '{3}', {4}, {5});
                """.format(d.strftime('%Y/%m/%d'), self.setter, self.grade.value, self.hold_color, self.pos[0], self.pos[1]))

        self.id = c.lastrowid
        conn.commit()
        return 1

    def modify_db(self, date_set, setter, grade, hold_color):
        success, d = Route.validate_date(date_set)
        if not success:
            return False
        conn = sqlite3.connect('db/fullcrimp.db')
        c = conn.cursor()
        c.execute("""
                     UPDATE routes SET set_at = '{0}', setter = '{1}', grade = '{2}', hold_color = '{3}' WHERE id = {4}
                  """.format(d.strftime('%Y/%m/%d'), setter, grade.value, hold_color, self.id))

        conn.commit()

        self.date_set = date_set
        self.setter = setter
        self.grade = grade
        self.hold_color = hold_color
        self.update_thumbnail_with_route_color()

    def delete_from_db(self):
        conn = sqlite3.connect('db/fullcrimp.db')
        c = conn.cursor()
        c.execute("""
                DELETE FROM routes WHERE id = {0}
                """.format(self.id))
        conn.commit()

        return -1

    @staticmethod
    def validate_date(d):
        date_split = d.split("/")
        if len(date_split) > 3:
            return False, None
        y, m, d = date_split
        if len(y) != 4:
            return False, None
        if len(m) < 1 or len(m) > 2:
            return False, None
        if len(d) < 1 or len(d) > 2:
            return False, None
        return True, date(int(y), int(m), int(d))

    @staticmethod
    def get_routes_from_db():
        conn = sqlite3.connect('db/fullcrimp.db')
        c = conn.cursor()
        c.execute("""
                    SELECT * FROM routes
                  """)
        route_rows = c.fetchall()
        routes = []
        for r in route_rows:
            r_id, r_set_at, r_setter, r_grade, r_hold_color, r_pos_x, r_pos_y = r
            grade = [g for g in GradeEnum if g.value == r_grade]
            if len(grade) == 0:
                raise Exception("Wrong grade enum in database: " + r[2])
            routes.append(Route(grade[0], [float(r_pos_x), float(r_pos_y)], r_setter, r_set_at, r_hold_color, r_id))

        return routes



