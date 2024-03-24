import math

import matplotlib.pyplot as plt
import numpy as np

import file_parse


def generate_measurements_data(states, landmarks):
    noisy_odoms = []
    odoms = []
    for i in range(len(states) - 1):
        j = i + 1
        xi = states[i][0]
        xj = states[j][0]
        yi = states[i][1]
        yj = states[j][1]
        thetai = states[i][2]
        thetaj = states[j][2]
        delta_rot1 = math.atan2(yj - yi, xi - xj) - thetai
        delta_trans = ((xj - xi) ** 2 + (yj - yi) ** 2) ** 0.5
        delta_rot2 = thetaj - thetai - delta_rot1
        delta_cap_rot1 = np.random.normal(delta_rot1, 0.05 ** 2)
        delta_cap_rot2 = np.random.normal(delta_rot2, 0.05 ** 2)
        delta_cap_trans = np.random.normal(delta_trans, 0.1 ** 2)
        noisy_odoms.append((delta_cap_rot1, delta_cap_trans, delta_cap_rot2))
        odoms.append((delta_rot1, delta_trans, delta_rot2))
    bij_caps = []
    bijs = []
    for i in range(1, len(states)):
        state_bij_caps = []
        state_bijs = []
        for j in range(len(landmarks)):
            xi = states[i][0]
            yi = states[i][1]
            thetai = states[i][2]
            ylj = landmarks[j][1]
            xlj = landmarks[j][0]
            bij = math.atan2(ylj - yi, xlj - xi) - thetai
            bij_cap = np.random.normal(bij, 0.0523599 ** 2)
            state_bij_caps.append(bij_cap)
            state_bijs.append(bij)
        bij_caps.append(state_bij_caps)
        bijs.append(state_bijs)
    return noisy_odoms, bij_caps, odoms, bijs


def plot_differences(differences_rot1, differences_rot2, differences_trans, differences_bij):
    plt.title("Differences in rot1")
    plt.bar(range(len(differences_rot1)), differences_rot1)
    plt.show()
    plt.title("Differences in rot2")
    plt.bar(range(len(differences_rot2)), differences_rot2)
    plt.show()
    plt.title("Differences in trans")
    plt.bar(range(len(differences_trans)), differences_trans)
    plt.show()
    plt.title("Differences in bij")
    plt.bar(range(len(differences_bij)), differences_bij)
    plt.show()


def create_measurements_files(gt_trajs_ids, landmark_ids):
    differences_rot1 = []
    differences_rot2 = []
    differences_trans = []
    differences_bij = []
    for i in gt_trajs_ids:
        for j in landmark_ids:
            states = file_parse.parse_gt_trajectories(i)
            landmarks = file_parse.parse_landmarks(j)
            n_odoms, bij_caps, odoms, bijs = generate_measurements_data(states, landmarks)
            with open("measurement_data/measurements_{}_{}".format(i, j), "w") as mf:
                mf.write("{} {} {}\n".format(states[0][0], states[0][1], states[0][2]))
                mf.write(str(len(states) - 1))
                for m in range(len(states) - 1):
                    mf.write("{} {} {}\n".format(n_odoms[m][0], n_odoms[m][1], n_odoms[m][2]))
                    differences_rot1.append(abs(n_odoms[m][0] - odoms[m][0]))
                    differences_trans.append(abs(n_odoms[m][1] - odoms[m][1]))
                    differences_rot2.append(abs(n_odoms[m][2] - odoms[m][2]))
                    differences_bij.append(abs(((sum(bijs[m]) / len(bijs[m])) - (sum(bij_caps[m]) / len(bij_caps[m])))))
                    plot_differences(differences_rot1, differences_rot2, differences_trans, differences_bij)
                    for bij_cap in bij_caps[m]:
                        mf.write("{} ".format(bij_cap))
                    mf.write("\n")


if __name__ == '__main__':
    create_measurements_files([0], [0, 1, 2])
