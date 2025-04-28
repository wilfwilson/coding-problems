class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        if num == 1 or num == 4:
            return True

        lo = 1
        hi = int(num / 2)

        while lo < hi - 1:
            mid = int((lo + hi) / 2)
            x = mid * mid
            if x == num:
                return True
            elif x < num:
                lo = mid
            else:
                hi = mid

        return False
