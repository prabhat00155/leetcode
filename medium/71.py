"""Simplify Path
https://leetcode.com/problems/simplify-path
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path:
            return
        stk = []
        for d in path.split('/'):
            if d in ['', '.']:
                continue
            elif d == '..':
                if len(stk) > 0:
                    stk.pop()
            else:
                stk.append(d)
        return f'/{"/".join(stk)}'


def test(path: str):
    print(Solution().simplifyPath(path))


test('/home/')
test('/home//foo/')
test('/home/user/Documents/../Pictures')
test('/../')
test('/.../a/../b/c/../d/./')
