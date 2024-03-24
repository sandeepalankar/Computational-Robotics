from robot import Robot


def isCollisionFree(robot_dims, point, env_dim=100):
    temp_robot = Robot(robot_dims[0], robot_dims[1])
    temp_robot.set_pose(point)
    temp_robot.transform()
    n = len(temp_robot.robot_current_state)
    for i in range(n):
        j = (i + 1) % n
        p1 = temp_robot.robot_current_state[i]
        p2 = temp_robot.robot_current_state[j]
        if p1[0] < 0 or p1[0] > env_dim or p1[1] < 0 or p1[1] > env_dim or p2[0] < 0 or p2[0] > env_dim or p2[1] < 0 \
                or p2[1] > env_dim:
            return False
    return True
