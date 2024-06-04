"""Top K Frequent Words
https://leetcode.com/problems/top-k-frequent-words
"""


from heapq import heappush, heappop


class Node:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, other):
        return (
            self.freq < other.freq if self.freq != other.freq
            else self.word < other.word
        )


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        heap = []
        freq_map = {}
        output = []
        i = 0
        for word in words:
            freq_map[word] = freq_map.get(word, 0) + 1
        for key, v in freq_map.items():
            n = Node(key, -v)
            heappush(heap, n)
        while len(heap) > 0 and i < k:
            e = heappop(heap)
            output.append(e.word)
            i += 1
        return output


def test(words, k):
    print(Solution().topKFrequent(words, k))


test(["i", "love", "leetcode", "i", "love", "coding"], 2)
test(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
     4)
