# Finds the index of the first occurrence of <needle> in <haystack>,
# both strings of lowercase letters, with
# 1 <= haystack.length, needle.length <= 104.
# Returns -1 if there is no match.
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)

        # Check if <needle> starts at each possible position <i> of <haystack>
        for i in range(m - n + 1):
            j = 0
            while j < n and haystack[i + j] == needle[j]:
                j += 1
            
            # All <j> letters of <needle> appear in order in <haystack>, from pos <i>
            if n == j:
                return i

        # No match
        return -1
