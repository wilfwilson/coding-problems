class Solution:
    def romanToInt(self, s: str) -> int:
        value = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        prefixes = {"I": ["V", "X"], "X": ["L", "C"], "C": ["D", "M"]}

        n = len(s)
        out = 0
        i = 0
        while i < n:
            val = value[s[i]]
            if i < n - 1 and s[i] in prefixes and s[i + 1] in prefixes[s[i]]:
                out -= val
                out += value[s[i + 1]]
                i += 2
            else:
                out += val
                i += 1

        return out
