class Solution:
    def addDigits(self, num: int) -> int:
        # Answer is num % 9, unless num % 9 = 0, in which case answer is 9.
        # So code could be:
        ### return 0 if num == 0 else 1 + (num - 1) % 9
        def breakdown(x):
            out = 0
            while x > 9:
                r = x % 10
                x = x // 10
                out += r
            out += x
            return out

        while num > 9:
            num = breakdown(num)

        return num
