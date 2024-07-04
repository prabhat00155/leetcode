"""Integer to English Words
https://leetcode.com/problems/integer-to-english-words
"""


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'

        singles = {
            0: '',
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
        }
        doubles = {
            0: '',
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen',
            20: 'Twenty',
            30: 'Thirty',
            40: 'Forty',
            50: 'Fifty',
            60: 'Sixty',
            70: 'Seventy',
            80: 'Eighty',
            90: 'Ninety',
        }

        joiner = [
            ' Thousand ',
            ' Million ',
            ' Billion ',
            ' Trillion ',
        ]

        def triplet(n):
            if n == 0:
                return ''
            d1 = n // 100
            d2 = (n % 100) // 10
            d3 = n % 10
            prefix = '' if d1 == 0 else f'{singles[d1]} Hundred '
            if d3 == 0 or 10 <= d2 * 10 + d3 <= 19:
                return f'{prefix}{doubles[d2 * 10 + d3]}'.strip()
            sep = '' if d2 == 0 else ' '
            return f'{prefix}{doubles[d2 * 10]}{sep}{singles[d3]}'.strip()

        output = ''
        count = -1
        while num > 0:
            if num % 1000 != 0:
                output = (f'{triplet(num % 1000)}{joiner[count]}{output}'
                          if count != -1 else triplet(num % 1000))
            num = num // 1000
            count += 1
        return output.strip()


def test(num):
    print(Solution().numberToWords(num))


test(123)
test(0)
test(12345)
test(1002)
