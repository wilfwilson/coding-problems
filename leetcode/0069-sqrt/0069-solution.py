class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        lo = 1
        hi = int(x / 2) + 1
        while lo < hi - 1:
            mid = int((lo + hi) / 2)
            if mid * mid < x:
                lo = mid
            else:
                hi = mid

        if hi * hi == x:
            return hi
        else:
            return lo
