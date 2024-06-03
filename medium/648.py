"""Replace Words
https://leetcode.com/problems/replace-words
"""


class Node:
    def __init__(self, val=None):
        self.val = val
        self.is_leaf = False
        self.children = [None] * 26


class Trie:
    def __init__(self, node):
        self.root = node

    def add(self, word):
        if not word:
            return

        def insert(node, word):
            if not word:
                node.is_leaf = True
                return
            c = word[0]
            index = ord(c) - ord('a')
            if node.children[index] is None:
                n = Node(c)
                node.children[index] = n
            insert(node.children[index], word[1:])

        insert(self.root, word)

    def find(self, word):
        if not word:
            return word

        def find_smallest(node, word, cur):
            if node.is_leaf:
                return cur
            if not word:
                return None
            c = word[0]
            cur = f'{cur}{c}'
            index = ord(c) - ord('a')
            if node.children[index] and node.children[index].val == c:
                if node.children[index].is_leaf:
                    return cur
                return find_smallest(node.children[index], word[1:], cur)

            return None
        ret = find_smallest(self.root, word, '')
        return ret if ret else word


class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        trie = Trie(Node())
        res = []
        for word in dictionary:
            trie.add(word)
        for word in sentence.split():
            res.append(trie.find(word))
        return ' '.join(res)


def test(dictionary, sentence):
    print(Solution().replaceWords(dictionary, sentence))


test(["cat", "bat", "rat"], "the cattle was rattled by the battery")
test(["a", "b", "c"], "aadsfasf absbs bbab cadsfafs")
