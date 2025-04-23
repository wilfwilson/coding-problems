class Solution:
    # Add one to an integer represented as an array
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        # Work from the end of the list, and increment the digits mod 10
        # until we reach a digit < 9, or run out of digits
        i = 0
        while i < n:
            i += 1
            if digits[n - i] != 9:
                digits[n - i] += 1
                return digits
            digits[n - i] = 0

        # If we reach here, then every element of digits was equal to 9
        return [1] + digits
