"""Ones and Zeroes
https://leetcode.com/problems/ones-and-zeroes
"""


class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        mapper = {}

        def count(item):
            count_0 = item.count('0')
            count_1 = len(item) - count_0
            return count_0, count_1

        def find_max(index, rem_0, rem_1):
            if index >= len(strs):
                return 0
            if (index, rem_0, rem_1) not in mapper:
                without_current = find_max(index + 1, rem_0, rem_1)
                count_0, count_1 = counter[index]
                if count_0 <= rem_0 and count_1 <= rem_1:
                    with_current = 1 + find_max(
                        index + 1, rem_0 - count_0, rem_1 - count_1)
                    mapper[(index, rem_0, rem_1)] = max(
                        without_current, with_current)
                else:
                    mapper[(index, rem_0, rem_1)] = without_current
            return mapper[(index, rem_0, rem_1)]

        counter = [count(item) for item in strs]
        return find_max(0, m, n)


def test(strs, m, n):
    print(Solution().findMaxForm(strs, m, n))


test(["10", "0001", "111001", "1", "0"], 5, 3)
test(["10", "0", "1"], 1, 1)
