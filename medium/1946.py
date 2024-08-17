"""Largest Number After Mutating Substring
https://leetcode.com/problems/largest-number-after-mutating-substring
"""


class Solution:
    def maximumNumber(self, num: str, change: list[int]) -> str:
        output, changed = '', False
        for index, val in enumerate(num):
            i = ord(val) - ord('0')
            if change[i] > int(val):
                output = f'{output}{change[i]}'
                changed = True
            elif changed and change[i] != int(val):
                output = f'{output}{num[index:]}'
                break
            else:
                output = f'{output}{val}'
        return output


def test(num: str, change: list[int]):
    print(Solution().maximumNumber(num, change))


test('132', [9, 8, 5, 0, 3, 6, 4, 2, 6, 8])
test('021', [9, 4, 3, 5, 7, 2, 1, 9, 0, 6])
test('5', [1, 4, 7, 5, 3, 2, 5, 6, 9, 4])
