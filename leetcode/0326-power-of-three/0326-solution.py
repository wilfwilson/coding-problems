class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Naive way
        while n > 1 and n % 3 == 0:
            n = int(n / 3)
        return n == 1
