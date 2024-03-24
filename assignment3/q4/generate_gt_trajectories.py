import random

import numpy as np

import collision


def generate_random_trajectory(robot_dims, start, max_translation, max_rotation):
    states = [start]

    while len(states) < 101:
        delta_translation = random.uniform(0, max_translation)
        delta_rotation_1 = random.uniform(-max_rotation, max_rotation)
        delta_rotation_2 = random.uniform(-max_rotation, max_rotation)
        new_x = states[-1][0] + delta_translation * np.cos(states[-1][2] + delta_rotation_1)
        new_y = states[-1][1] + delta_translation * np.sin(states[-1][2] + delta_rotation_1)
        new_theta = (states[-1][2] + delta_rotation_1 + delta_rotation_2) % (2 * np.pi)
        if collision.isCollisionFree(robot_dims, (new_x, new_y, new_theta)):
            states.append((new_x, new_y, new_theta))
        else:
            delta_rotation_1 += np.pi / 2
            delta_rotation_2 += np.pi
            new_x = states[-1][0] + delta_translation * np.cos(states[-1][2] + delta_rotation_1)
            new_y = states[-1][1] + delta_translation * np.sin(states[-1][2] + delta_rotation_1)
            new_theta = (states[-1][2] + delta_rotation_1 + delta_rotation_2) % (2 * np.pi)
            states.append((new_x, new_y, new_theta))
    return states


def generate_gt_trajectories():
    for i in range(3):
        with open("gt_trajectories/ground_truth_{}.txt".format(i), "w") as gtf:
            gtf.write("101\n")
            random_traj = generate_random_trajectory((2, 3), (30, 30, 0), 1, np.pi / 6)
            for t in random_traj:
                gtf.write("{} {} {}\n".format(round(t[0], 2), round(t[1], 2), round(t[2], 2)))


if __name__ == '__main__':
    generate_gt_trajectories()
