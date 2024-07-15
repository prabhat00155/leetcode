"""Most Frequent Prime
https://leetcode.com/problems/most-frequent-prime
"""


class Solution:
    def mostFrequentPrime(self, mat: list[list[int]]) -> int:
        freq = {}

        def is_prime(num):
            for d in range(2, num//2):
                if num % d == 0:
                    return False
            return num > 1

        def possibilities(row, col, row_dir, col_dir, val):
            if 0 <= row < len(mat) and 0 <= col < len(mat[0]):
                val = val * 10 + mat[row][col]
                if val > 10 and is_prime(val):
                    freq[val] = freq.get(val, 0) + 1
                possibilities(row+row_dir, col+col_dir, row_dir, col_dir, val)

        def maxima():
            if not freq:
                return -1
            max_value = max(freq.values())
            max_keys = [k for k, v in freq.items() if v == max_value]
            return max(max_keys)

        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        ]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                for (r_dir, c_dir) in directions:
                    possibilities(i, j, r_dir, c_dir, 0)

        return maxima()


def test(mat):
    print(Solution().mostFrequentPrime(mat))


test([[1, 1], [9, 9], [1, 1]])
test([[7]])
test([[9, 7, 8], [4, 6, 5], [2, 8, 6]])
