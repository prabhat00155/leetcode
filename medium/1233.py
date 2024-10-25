"""Remove Sub-Folders from the Filesystem
https://leetcode.com/problems/remove-sub-folders-from-the-filesystem
"""


class TrieNode:
    def __init__(self):
        self.nodes = {}
        self.is_leaf = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, s):
        node = self.root
        for c in s.split('/'):
            if not c:
                continue
            if c not in node.nodes:
                node.nodes[c] = TrieNode()
            node = node.nodes[c]
        node.is_leaf = True

    def search(self, s):
        node = self.root
        for c in s.split('/'):
            if not c:
                continue
            if c not in node.nodes:
                break
            node = node.nodes[c]
        return node.is_leaf


class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        folder.sort(key=len)
        output = []
        trie = Trie()
        for f in folder:
            if not trie.search(f):
                output.append(f)
                trie.add(f)
        return output


def test(folder: list[str]) -> list[str]:
    return Solution().removeSubfolders(folder)


assert test(["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]) == ["/a", "/c/d", "/c/f"]
assert test(["/a", "/a/b/c", "/a/b/d"]) == ["/a"]
assert test(["/a/b/c", "/a/b/ca", "/a/b/d"]) == ["/a/b/c", "/a/b/d", "/a/b/ca"]
