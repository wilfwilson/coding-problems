class Solution:
    def toHex(self, num: int) -> str:

        if num == 0:
            return "0"

        lookup = "0123456789abcdef"
        out = ""

        # Two's complement: convert negative to positive to use the same code below
        if num < 0:
            num += 2 ** 32

        while num > 0:
            x = num % 16
            out += lookup[x]
            num = int((num - x) / 16)

        return out[::-1]
