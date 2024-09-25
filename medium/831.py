"""Masking Personal Information
https://leetcode.com/problems/masking-personal-information
"""


class Solution:
    def maskPII(self, s: str) -> str:
        def mask_email():
            name, domain = s.lower().split('@')
            return f'{name[0]}*****{name[-1]}@{domain}'

        def mask_number():
            digits = ''
            for c in s:
                if c.isdigit():
                    digits = f'{digits}{c}'
            return (
                f'{"+" if len(digits) > 10 else ""}'
                f'{"*" * (len(digits) - 10)}'
                f'{"-" if len(digits) > 10 else ""}***-***-{digits[-4:]}'
            )

        return mask_email() if '@' in s else mask_number()


def test(s: str):
    print(Solution().maskPII(s))


test('LeetCode@LeetCode.com')
test('AB@qq.com')
test('1(234)567-890')
