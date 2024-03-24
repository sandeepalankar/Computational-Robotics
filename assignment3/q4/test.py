import file_parse
import visualizer
from robot import Robot


def test_parse_visualizer():
    landmarks = file_parse.parse_landmarks("0")
    states = file_parse.parse_gt_trajectories("0")
    robot = Robot(2, 3)
    visualizer.visualize_problem(robot, landmarks, states)


if __name__ == '__main__':
    test_parse_visualizer()
