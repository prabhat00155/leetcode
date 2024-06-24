"""Count Ways to Build Rooms in an Ant Colony
https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony
"""


import collections
import math


class Solution:
    def waysToBuildRooms(self, prevRoom: list[int]) -> int:
        edges = collections.defaultdict(list)
        MOD = 10 ** 9 + 7

        for index, value in enumerate(prevRoom):
            edges[value].append(index)

        def find_ways(u):
            if not edges[u]:
                return 1, 1
            res, left = 1, 0
            for v in edges[u]:
                tmp, right = find_ways(v)
                res = (res * tmp * math.comb(left+right, right)) % MOD
                left += right
            return res, left + 1

        return find_ways(0)[0]


def test(prev_room):
    print(Solution().waysToBuildRooms(prev_room))


test([-1, 0, 1])
test([-1, 0, 0, 1, 2])
