class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        word_to_pattern_letter = {}
        pattern_letter_to_word = {}
        
        def nextWord(s, i):
            out = ""
            while i < len(s) and s[i] != ' ':
                out += s[i]
                i += 1
            i += 1
            return out, i

        i = 0
        j = 0
        while i < len(pattern) and j < len(s):

            x, j = nextWord(s, j)

            if pattern[i] in pattern_letter_to_word:
                if pattern_letter_to_word[pattern[i]] != x:
                    return False
            else:
                pattern_letter_to_word[pattern[i]] = x

            if x in word_to_pattern_letter:
                if word_to_pattern_letter[x] != pattern[i]:
                    return False
            else:
                word_to_pattern_letter[x] = pattern[i]

            i += 1

        return i == len(pattern) and j == len(s) + 1
