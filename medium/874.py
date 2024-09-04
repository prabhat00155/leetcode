"""Walking Robot Simulation
https://leetcode.com/problems/walking-robot-simulation
"""


class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        x_pos, y_pos = 0, 0
        x_dir, y_dir = 0, 1
        max_dist = 0
        map_left = {
            (0, 1): (-1, 0),
            (-1, 0): (0, -1),
            (0, -1): (1, 0),
            (1, 0): (0, 1),
        }
        map_right = {
            (0, 1): (1, 0),
            (1, 0): (0, -1),
            (0, -1): (-1, 0),
            (-1, 0): (0, 1),
        }
        obstacles_set = set([(o[0], o[1]) for o in obstacles])
        for command in commands:
            if command == -2:
                x_dir, y_dir = map_left[(x_dir, y_dir)]
            elif command == -1:
                x_dir, y_dir = map_right[(x_dir, y_dir)]
            else:
                for i in range(command):
                    if (x_pos + x_dir, y_pos + y_dir) in obstacles_set:
                        break
                    x_pos, y_pos = x_pos + x_dir, y_pos + y_dir
                    max_dist = max(max_dist, x_pos*x_pos+y_pos*y_pos)
        return max_dist


def test(commands: list[int], obstacles: list[list[int]]):
    print(Solution().robotSim(commands, obstacles))


test([4, -1, 3], [])
test([4, -1, 4, -2, 4], [[2, 4]])
test([6, -1, -1, 6], [])
