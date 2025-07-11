class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Pass through the string once, indexed by i.
        #
        # Have a dictionary which is updated as we pass through, where for
        # each character that we encounter, we save its most recently-seen
        # position.
        #
        # Keep track of the index of the starting point of the longest known
        # unique-character substring that includes position i.
        #
        # Also keep track of the maximum length of a unique-character substring
        # that we've seen.
        characters = {}
        start = 0
        maxlen = 0
        for i in range(len(s)):
            if s[i] in characters and characters[s[i]] >= start:
                # The character s[i] occurs at both position i and position
                # characters[s[i]]. Therefore the longest known unique-character
                # substring that includes position i excludes position
                # characters[s[i]], but starts straight afterwards.
                start = characters[s[i]] + 1
            else:
                # The character s[i] extends the length of the substring that we
                # we previously considering. Therefore we might have found a new
                # longest length: calculate.
                maxlen = max(maxlen, i - start + 1)

            # Record that we most-recently saw s[i] in position i
            characters[s[i]] = i
        return maxlen
