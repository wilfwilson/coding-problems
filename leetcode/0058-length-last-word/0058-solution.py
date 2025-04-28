class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1

        # Skip over trailing whitespace to find the end of the word
        while i > 0 and s[i] == " ":
            i -= 1

        # Save where the word ends
        end = i

        # Count non-whitespace characters
        while i >= 0 and s[i] != " ":
            i -= 1

        return end - i
