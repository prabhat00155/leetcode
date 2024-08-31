"""Count Days Without Meetings
https://leetcode.com/problems/count-days-without-meetings
"""


class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        meetings.sort()
        count = meetings[0][0] - 1
        end = meetings[0][1]
        for i in range(1, len(meetings)):
            if meetings[i][0] > end:
                count += meetings[i][0] - end - 1
            end = max(meetings[i][1], end)
        count += days - end
        return count


def test(days: int, meetings: list[list[int]]):
    print(Solution().countDays(days, meetings))


test(10, [[5, 7], [1, 3], [9, 10]])
test(5, [[2, 4], [1, 3]])
test(6, [[1, 6]])
