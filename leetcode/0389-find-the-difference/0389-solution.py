class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        xor = 0
        for x in s:
            xor ^= ord(x)
        for x in t:
            xor ^= ord(x)
        return chr(xor)
