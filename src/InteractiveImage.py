from kivy.uix.image import Image

from src.ProblemCreationState import ProblemCreationState
from src.Grade import GradeEnum
from src.Route import Route

import imageio.v3 as iio
import numpy as np


class InteractiveImage(Image):
    points = []
    scatterPlane = None
    state: ProblemCreationState = ProblemCreationState.NONE
    newImageCreated = False
    original_source = ""
    routes = []
    grade_enum: GradeEnum = GradeEnum.EASY
    image_size = [1, 1]
    window_size = [1, 1]
    scale = 1
    setter = None

    modify = None

    def add_routes_to_image(self):
        if not self.newImageCreated:
            self.original_source = self.source

        img = np.array(iio.imread(self.source))
        for route in self.routes:
            y_offset = route.x_offset
            x_offset = route.y_offset
            # Ensure transparency
            x0 = max(0, x_offset)
            y0 = max(0, y_offset)
            x1 = min(img.shape[0], x_offset + route.img.shape[0])
            y1 = min(img.shape[1], y_offset + route.img.shape[1])

            route_patch = img[x0:x1, y0:y1]
            if route_patch.shape[0] == 0:
                continue

            overlay_img = route.img.copy()

            x0_overlay = x_offset - max(x_offset, 0)
            x1_overlay = route.img.shape[0] - (x_offset + route.img.shape[0] - min(x_offset + route.img.shape[0], img.shape[0]))
            y0_overlay = y_offset - max(y_offset, 0)
            y1_overlay = route.img.shape[1] - (y_offset + route.img.shape[1] - min(y_offset + route.img.shape[1], img.shape[1]))

            overlay_img = overlay_img[x0_overlay:x1_overlay, y0_overlay:y1_overlay]

            transparent_indices = np.where(np.sum(overlay_img, axis=2) == 0)

            if len(transparent_indices) == 0:
                continue

            overlay_img[transparent_indices] = route_patch[transparent_indices]

            img[x0:x1, y0:y1] = overlay_img

        if not self.newImageCreated:
            filename = self.source.split("/")[-1]
            filename = filename[:filename.index(".")] + "new.png"
            filename = "/".join(self.source.split("/")[:-1]) + "/" + filename
        else:
            filename = self.source

        self.newImageCreated = True

        iio.imwrite(filename, img)
        self.source = filename
        self.reload()

    def try_delete_route(self, pos):
        route_deleted = False
        for route in reversed(self.routes):
            if route.is_point_inside(pos):
                self.routes.remove(route)
                route.delete_from_db()
                route_deleted = True
                break
        if not route_deleted:
            return

        self.source = self.original_source
        self.newImageCreated = False

    def try_modify_route(self, pos):
        route_modified = False
        for route in reversed(self.routes):
            if route.is_point_inside(pos):
                route_modified = True
                self.modify(route)
                break
        if not route_modified:
            return

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)

            yscale = 0.45
            miny = self.center_y - self.image_size[0] * yscale / 2
            maxy = self.center_y + self.image_size[0] * yscale / 2
            if maxy < touch.pos[1] < miny:
                return super().on_touch_down(touch)

            xscale = 0.4479
            minx = self.center_x - self.image_size[1] * yscale / 2
            maxx = self.center_x + self.image_size[1] * yscale / 2

            scaled_pos = ((touch.pos[0] - minx) / xscale, (maxy - touch.pos[1]) / yscale)
            self.points = [*touch.pos]
            print(self.points, scaled_pos, xscale, yscale, self.scale)
            if self.state == ProblemCreationState.ADD:
                self.add_route(self.grade_enum, scaled_pos)
            elif self.state == ProblemCreationState.DELETE:
                self.try_delete_route(scaled_pos)
            elif self.state == ProblemCreationState.MODIFY:
                if self.modify is not None:
                    self.try_modify_route(scaled_pos)

            self.add_routes_to_image()

        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        if touch.grab_current == self:
            self.points.extend(touch.pos)
        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        if touch.grab_current == self:
            touch.ungrab(self)
            self.points.extend(touch.pos)
        return super().on_touch_up(touch)

    def clear(self):
        self.points = []

    def add_route(self, grade, pos):
        route = Route(grade, pos, self.setter())
        route.add_route_to_db()
        self.routes.append(route)