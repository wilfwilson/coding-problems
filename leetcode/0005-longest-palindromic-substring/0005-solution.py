class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for x in range(n)]
        result = [0, 0]

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                result = [i, i + 1]

        for diff in range(2, n):
            for i in range(n - diff):
                if s[i] == s[i + diff] and dp[i + 1][i + diff - 1]:
                    dp[i][i + diff] = True
                    result = [i, i + diff]

        return s[result[0]:result[1] + 1]
