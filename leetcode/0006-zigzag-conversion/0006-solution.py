class Solution:
    def convert(self, s: str, numRows: int) -> str:

        n = len(s)
        k = numRows
        out = ""

        # Edge cases
        if n <= k or k == 1:
            return s

        # first row
        index = 0
        while index < n:
            out += s[index]
            index += 2 * (k - 1)

        # middle rows
        for i in range(1, numRows - 1):
            index = i
            while index < n:
                out += s[index]
                index += 2 * (k - (i + 1))
                if index < n:
                    out += s[index]
                    index += 2 * i

        # last row
        index = numRows - 1
        while index < n:
            out += s[index]
            index += 2 * (k - 1)

        return out
