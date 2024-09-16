"""Minimum Time Difference
https://leetcode.com/problems/minimum-time-difference
"""


class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:

        def to_minutes(t):
            hh, mm = t.split(':')
            return int(hh) * 60 + int(mm)

        times = []
        MAXIMA = 24 * 60
        min_minutes = float('inf')
        for t in timePoints:
            times.append(to_minutes(t))
        times.sort()
        times.append(MAXIMA+times[0])
        for i in range(1, len(times)):
            min_minutes = min(min_minutes, abs(times[i]-times[i - 1]))
        return min_minutes


def test(time_points: list[str]):
    print(Solution().findMinDifference(time_points))


test(["23:59", "00:00"])
test(["00:00", "23:59", "00:00"])
