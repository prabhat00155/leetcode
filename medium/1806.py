"""Minimum Number of Operations to Reinitialize a Permutation
https://leetcode.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation
"""


class Solution:
    def reinitializePermutation(self, n: int) -> int:
        def is_equal(arr1, arr2):
            i = 0
            while i < len(arr1):
                if arr1[i] != arr2[i]:
                    return False
                i += 1
            return True

        def apply_operation(arr):
            tmp = list(arr)
            for i in range(len(arr)):
                if i % 2 == 0:
                    index = i // 2
                else:
                    index = n // 2 + (i - 1) // 2
                arr[i] = tmp[index]

        perm = [i for i in range(n)]
        arr = list(perm)
        count, flag = 0, True
        while flag:
            apply_operation(arr)
            count += 1
            if is_equal(perm, arr):
                flag = False
        return count


def test(n: int):
    print(Solution().reinitializePermutation(n))


test(2)
test(4)
test(6)
