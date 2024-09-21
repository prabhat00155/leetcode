"""Lexicographical Numbers
https://leetcode.com/problems/lexicographical-numbers
"""


class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        output = []
        digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        def dfs(num):
            if num > n:
                return
            output.append(num)
            for d in digits:
                dfs(num*10+d)

        for d in digits[1:]:
            dfs(d)
        return output


def test(n: int):
    print(Solution().lexicalOrder(n))


test(13)
test(2)
