"""Sum of Prefix Scores of Strings
https://leetcode.com/problems/sum-of-prefix-scores-of-strings
"""


class Node:
    def __init__(self):
        self.children = [None] * 26
        self.count = 0


class Trie:
    def __init__(self):
        self.root = Node()

    def _char_to_index(self, c):
        return ord(c) - ord('a')

    def insert(self, s):
        node = self.root
        for c in s:
            index = self._char_to_index(c)
            if not node.children[index]:
                node.children[index] = Node()
            node = node.children[index]
            node.count += 1

    def search(self, s):
        node = self.root
        count = 0
        for c in s:
            index = self._char_to_index(c)
            if not node.children[index]:
                return count
            node = node.children[index]
            count += node.count
        return count


class Solution:
    def sumPrefixScores(self, words: list[str]) -> list[int]:
        trie = Trie()
        answer = []
        for w in words:
            trie.insert(w)
        for w in words:
            answer.append(trie.search(w))
        return answer


def test(words: list[str]):
    print(Solution().sumPrefixScores(words))


test(["abc", "ab", "bc", "b"])
test(["abcd"])
