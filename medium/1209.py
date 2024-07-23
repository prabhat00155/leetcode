"""Remove All Adjacent Duplicates in String II
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii
"""


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = []
        for c in s:
            if stk and stk[-1][0] == c:
                stk[-1][1] += 1
                if stk[-1][1] == k:
                    stk.pop()
            else:
                stk.append([c, 1])
        return ''.join(c * count for c, count in stk)


def test(s, k):
    print(Solution().removeDuplicates(s, k))


test('abcd', 2)
test('deeedbbcccbdaa', 3)
test('pbbcggttciiippooaais', 2)
