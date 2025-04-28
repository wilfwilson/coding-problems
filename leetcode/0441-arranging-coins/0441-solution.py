class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Strategy: use some maths to the find the greatest triangular number <= n.

        x = int(math.sqrt(n * 2))
        if (x * (x + 1)) // 2 <= n:
            return x
        else:
            return x - 1
