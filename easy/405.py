"""Convert a Number to Hexadecimal
"""


class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'

        def pos_hex(num):
            res = ''
            while num > 0:
                rem = num % 16
                res = f'{rem if rem < 10 else chr(ord("a")+rem-10)}{res}'
                num //= 16
            return res

        def binary(num):
            res = ''
            while num > 0:
                rem = num % 2
                res = f'{rem}{res}'
                num //= 2
            return f'{"0" * (32 - len(res))}{res}'

        def flip_bits(s):
            res = []
            for c in s:
                res.append('1' if c == '0' else '0')
            return ''.join(res)

        def add_one(s):
            res, carry = '', True
            for c in reversed(s):
                if carry:
                    if c == '1':
                        res = f'0{res}'
                    else:
                        res = f'1{res}'
                        carry = False
                else:
                    res = f'{c}{res}'
            return res

        def binary_to_hex(binary):
            i = 0
            res = []
            while i + 3 < 32:
                cur = (
                    int(binary[i]) * 8 + int(binary[i + 1]) * 4
                    + int(binary[i + 2]) * 2 + int(binary[i + 3])
                )
                cur = str(cur) if cur < 10 else chr(ord('a')+cur-10)
                res.append(cur)
                i += 4
            return ''.join(res)

        def neg_hex(num):
            num = abs(num)
            bin_res = binary(num)
            bin_res = flip_bits(bin_res)
            bin_res = add_one(bin_res)
            return binary_to_hex(bin_res)

        return pos_hex(num) if num >= 0 else neg_hex(num)


def test(num: int):
    print(Solution().toHex(num))


test(26)
test(0)
test(-1)
test(1000)
