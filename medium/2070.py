"""Most Beautiful Item for Each Query

https://leetcode.com/problems/most-beautiful-item-for-each-query
"""


from bisect import bisect_left


class Solution:
    def maximumBeauty(
        self, items: list[list[int]], queries: list[int]
    ) -> list[int]:
        items.sort()
        buffer, output = [], []
        i, max_till_now = 0, -float('inf')
        while i < len(items) - 1:
            max_till_now = max(max_till_now, items[i][1])
            if items[i][0] != items[i + 1][0]:
                buffer.append([items[i][0], max_till_now])
            i += 1
        max_till_now = max(max_till_now, items[i][1])
        buffer.append([items[i][0], max_till_now])
        for q in queries:
            index = bisect_left(buffer, q, key=lambda x: x[0])
            if index < len(buffer) and buffer[index][0] == q:
                output.append(buffer[index][1])
            else:
                output.append(buffer[index - 1][1] if index > 0 else 0)
        return output


def test(items: list[list[int]], queries: list[int]) -> list[int]:
    return Solution().maximumBeauty(items, queries)


assert test(
    [[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]], [1, 2, 3, 4, 5, 6]
) == [2, 4, 5, 5, 6, 6]
assert test([[1, 2], [1, 2], [1, 3], [1, 4]], [1]) == [4]
assert test([[10, 1000]], [5]) == [0]
