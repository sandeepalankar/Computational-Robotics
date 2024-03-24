import math


class Robot:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.translation = (0, 0)
        self.rotation = 0
        self.robot_origin_coords = [(-self.width / 2, -self.height / 2), (-self.width / 2, self.height / 2),
                                    (self.width / 2, self.height / 2), (self.width / 2, -self.height / 2)]
        self.robot_rotated_coords = self.robot_origin_coords
        self.robot_current_state = self.robot_origin_coords

    def set_pose(self, pose):
        self.translation = (pose[0], pose[1])
        self.rotation = pose[2]

    def transform(self):
        self.rotate(self.rotation)
        self.robot_current_state = self.translate(self.translation)
        return self.robot_current_state

    def translate(self, target: tuple):
        new_x, new_y = target
        new_coords = []
        for c in self.robot_rotated_coords:
            new_coords.append((c[0] + new_x, c[1] + new_y))
        return new_coords

    def rotate(self, angle):
        new_coords = []
        for c in self.robot_origin_coords:
            ox, oy = (0, 0)
            px, py = c[0], c[1]

            qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
            qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
            new_coords.append((qx, qy))
        self.robot_rotated_coords = new_coords
        return new_coords
