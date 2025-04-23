class Solution:
    def isUgly(self, n: int) -> bool:

        # Special case negative numbers and zero
        if n <= 0:
            return False

        # Divide n to exhaustion by each of the primes 2, 3, 5.
        while n % 2 == 0:
            n = int(n / 2)
        while n % 3 == 0:
            n = int(n / 3)
        while n % 5 == 0:
            n = int(n / 5)
        
        # Ugly numbers are those with no primes left by this point.
        return n == 1
