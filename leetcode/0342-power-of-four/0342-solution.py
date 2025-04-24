class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Naive way
        # while n > 1 and n % 4 == 0:
        #     n = int(n / 4)
        # return n == 1

         # Bit-twiddling way
        return n > 0 and n & (n - 1) == 0 and n % 3 == 1
