"""Find the Length of the Longest Common Prefix
https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix
"""


class Node:
    def __init__(self):
        self.children = [None] * 10


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, num):
        node = self.root
        for c in str(num):
            index = int(c)
            if not node.children[index]:
                node.children[index] = Node()
            node = node.children[index]

    def search(self, num):
        node, matches = self.root, 0
        for c in str(num):
            index = int(c)
            if not node.children[index]:
                break
            matches += 1
            node = node.children[index]
        return matches


class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        trie, result = Trie(), 0
        for num in arr1:
            trie.insert(num)
        for num in arr2:
            result = max(result, trie.search(num))
        return result


def test(arr1: list[int], arr2: list[int]):
    print(Solution().longestCommonPrefix(arr1, arr2))


test([1, 10, 100], [1000])
test([1, 2, 3], [4, 4, 4])
