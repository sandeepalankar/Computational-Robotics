from matplotlib import pyplot as plt, animation
import numpy as np

import utils


class EnvironmentVisualizer:
    def __init__(self, environment, robot):
        self.environment = environment
        self.ax = None
        self.fig = None
        self.configure_plot()
        self.robot = robot
        self.box_environment()

    @staticmethod
    def show_environment():
        plt.show()

    def animate_path(self, path, robot, file_name="rrt.gif"):
        filler, = self.ax.plot([], [], 'r-')

        def update(i):
            xdata, ydata = [], []
            robot.set_pose(path[i])
            robot.transform()
            for x, y in robot.robot_current_state:
                xdata.append(x)
                ydata.append(y)
            xdata.append(robot.robot_current_state[0][0])
            ydata.append(robot.robot_current_state[0][1])
            filler.set_data(xdata, ydata)
            return filler,

        ani = animation.FuncAnimation(self.fig, update, frames=len(path), interval=50, blit=True, repeat=False)
        writergif = animation.PillowWriter(fps=30)
        ani.save(file_name, writer=writergif)
        self.show_environment()

    def animate_tree_construction(self, rrt_tree, file_name="rrt.png"):
        for p1, p2 in rrt_tree:
            self.ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color="k")
            plt.pause(0.01)
            plt.draw()
        plt.savefig(file_name)

    def configure_plot(self):
        self.fig = plt.figure(figsize=(7, 7))
        self.ax = plt.axes()
        self.ax.set_aspect("equal")
        return self.fig

    def box_environment(self):
        for row in range(self.environment.n_rows):
            for cell in range(self.environment.n_cols):
                i = row
                j = cell
                if i == 0:
                    self.ax.plot([0, (j + 1)], [i, i], color="k")
                if j == self.environment.n_cols - 1:
                    self.ax.plot([(j + 1), (j + 1)], [i, (i + 1)], color="k")
                if i == self.environment.n_rows - 1:
                    self.ax.plot([(j + 1), j], [(i + 1), (i + 1)], color="k")
                if j == 0:
                    self.ax.plot([j, j], [(i + 1), i], color="k")

    def fill_landmarks(self):
        for point in self.environment.landmarks:
            self.ax.plot(point[0], point[1], "co")

    def fill_environment(self):
        # self.fill_start_and_goal_coords()
        self.fill_obstacles()
        self.fill_robot()
        self.fill_landmarks()

    def fill_obstacles(self):
        for obstacle in self.environment.obstacles:
            self.ax.fill([a[0] for a in obstacle], [a[1] for a in obstacle], color="k")

    def fill_robot(self, color="blue"):
        self.ax.fill([a[0] for a in self.robot.robot_current_state], [a[1] for a in self.robot.robot_current_state],
                     color=color)

    def fill_any_robot(self, robot, color="blue"):
        self.ax.fill([a[0] for a in robot.robot_current_state], [a[1] for a in robot.robot_current_state],
                     color=color)

    def plot_path(self, path):
        for i in range(len(path) - 1):
            self.ax.plot([path[i][0], path[i + 1][0]], [path[i][1], path[i + 1][1]], color="k")

    def plot_tree(self):
        for k, v in self.environment.tree.tree.items():
            for pt in v:
                self.ax.plot([k[0], pt[0]], [k[1], pt[1]], color="k")


def discretize_points_for_animation(path):
    discretization_const = 0.05
    new_path = []
    for i in range(len(path) - 1):
        point1 = path[i]
        point2 = path[i + 1]
        i = point1
        new_x, new_y, new_theta = point1
        while True:
            len_ab = utils.state_dist((new_x, new_y, new_theta), point2)
            len_ratio = discretization_const / len_ab
            new_x = round((1 - len_ratio) * i[0] + len_ratio * point2[0], 3)
            new_y = round((1 - len_ratio) * i[1] + len_ratio * point2[1], 3)
            new_theta = round((1 - len_ratio) * i[2] + len_ratio * point2[2], 3)
            if utils.state_dist(point1, (new_x, new_y, new_theta)) < utils.state_dist(point1, point2):
                i = new_x, new_y, new_theta
                new_path.append(i)
            else:
                new_path.append(point2)
                break
    return new_path