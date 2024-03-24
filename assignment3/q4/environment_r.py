from typing import List

from visualizer_utils import EnvironmentVisualizer


class Environment:

    def __init__(self, n_rows, n_cols, tree=None):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.start = None
        self.end = None
        self.obstacles = []
        self.landmarks = []
        self.tree = tree

    def set_start_state(self, coords):
        x, y, theta = coords
        self.start = (x, y, theta)

    def set_end_state(self, coords):
        x, y, theta = coords
        self.end = (x, y, theta)

    def create_obstacle(self, obstacle_coords=List[tuple]):
        self.obstacles.append(obstacle_coords)

    def add_landmarks(self, landmarks):
        for lm in landmarks:
            self.landmarks.append((lm[0], lm[1]))


class EnvSimulator:
    def __init__(self, env_x, env_y, robot):
        self.env = Environment(env_x, env_y)
        self.robot = robot
        self.env_vis = EnvironmentVisualizer(self.env, self.robot)


