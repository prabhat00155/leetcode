"""2 Keys Keyboard
https://leetcode.com/problems/2-keys-keyboard
"""


class Solution:
    def minSteps(self, n: int) -> int:
        mapper = {}

        def steps(cur_state, clipboard):
            if len(cur_state) == n:
                return 0
            if len(cur_state) > n:
                return float('inf')
            if (cur_state, clipboard) not in mapper:
                if len(f'{cur_state}{clipboard}') == n:
                    mapper[(cur_state, clipboard)] = 0
                else:
                    res1 = (
                        steps(f'{cur_state}{clipboard}', clipboard)
                        if clipboard else float('inf')
                    )
                    clipboard = f'{cur_state}{clipboard}'
                    res2 = 1 + steps(clipboard, clipboard)
                    mapper[(cur_state, clipboard)] = 1 + min(res1, res2)
            return mapper[(cur_state, clipboard)]
        return steps('A', '')


def test(n: int):
    print(Solution().minSteps(n))


test(3)
test(1)
