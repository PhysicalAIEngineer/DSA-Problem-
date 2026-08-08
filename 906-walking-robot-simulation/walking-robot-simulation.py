# Brute Force Code & Optimal Code
class Solution:
    def robotSim(self, commands, obstacles):
        # store all obstacle coordinates in a set each obstacle is represented as: (x, y) convert it into a string key: (2, 3) -> "2_3" this allows us to quickly check whether the robot's next position contains an obstacle.
        st = set()
        for obs in obstacles:
            # create a unique key for the obstacle position.
            key = str(obs[0]) + "_" + str(obs[1])
            # add the obstacle position to the set.
            st.add(key)
        # robot starts at the origin: (0, 0)
        x = 0
        y = 0
        # store the maximum squared distance reached by the robot from the origin initially, the robot is at (0, 0): distance^ = 0^2 + 0^2 = 0
        maxD = 0
        # robot initially faces north represent the direction using: (dx, dy) north = (0, 1) therefore, moving one step North means: x = x + 0 & y = y + 1
        dir = (0, 1)
        # process every command one by one.
        for command in commands:
            # case 1: -2 means turn left by 90 degrees direction transformation: (dx, dy) -> (-dy, dx)
            if command == -2:
                dir = (-dir[1], dir[0])
            # case 2: -1 means turn right by 90 degrees direction transformation: (dx, dy) -> (dy, -dx)
            elif command == -1:
                dir = (dir[1], -dir[0])
            # case 3: positive command means move forward. robot needs to move forward 4 steps move one step at a time because an obstacle can exist anywhere along the path
            else:
                for step in range(command):
                    # calculate the next position.
                    # 1. current position: (x, y)
                    # 2. direction: (dx, dy)
                    # 3. next position: (x + dx, y + dy)
                    newX = x + dir[0]
                    newY = y + dir[1]
                    # Create a key representing the next position.
                    nextKey = (str(newX) + "_" + str(newY))
                    # check whether the next position contains
                    # an obstacle if it does, the robot cannot move there stop the current movement command.
                    if nextKey in st:
                        break
                    # no obstacle exists move the robot to the new position
                    x = newX
                    y = newY
            # calculate the squared distance from the origin. formula: distance^2 = x^2 + y^2
            maxD = max(maxD, x * x + y * y)
        # return the maximum squared distance reached by the robot.
        return maxD

# Time Complexity : O(N)
# Space Complexity : O(N)