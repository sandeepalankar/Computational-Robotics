from environment_r import EnvSimulator
import matplotlib.pyplot as plt


def visualize_problem(robot, landmarks, groundtruths):
    env_sim = EnvSimulator(100, 100, robot)

    #env_sim.env.set_start_state(start)
    #env_sim.env.set_end_state(goal)
    env_sim.env.add_landmarks(landmarks)

    #env_sim.robot.set_pose(env_sim.env.start)
    env_sim.robot.transform()
    env_sim.env_vis.fill_robot(color="blue")
    env_sim.env_vis.fill_landmarks()
    #for o in obstacles:
        #env_sim.env.create_obstacle(o)

    for groundtruth in groundtruths:
        plt.scatter(groundtruth[0], groundtruth[1], color='green') 
        plt.plot()
    env_sim.env_vis.fill_obstacles()
   # env_sim.robot.set_pose(env_sim.env.end)
    #env_sim.robot.transform()
    env_sim.env_vis.fill_robot(color="green")
    env_sim.env_vis.show_environment()

