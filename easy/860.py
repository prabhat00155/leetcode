"""Lemonade Change
https://leetcode.com/problems/lemonade-change
"""


class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        freq = {5: 0, 10: 0, 20: 0}
        for b in bills:
            freq[b] += 1
            if b == 10:
                if freq[5] > 0:
                    freq[5] -= 1
                else:
                    return False
            elif b == 20:
                if freq[10] > 0 and freq[5] > 0:
                    freq[10] -= 1
                    freq[5] -= 1
                elif freq[5] >= 3:
                    freq[5] -= 3
                else:
                    return False
        return True


def test(bills: list[int]):
    print(Solution().lemonadeChange(bills))


test([5, 5, 5, 10, 20])
test([5, 5, 10, 10, 20])
