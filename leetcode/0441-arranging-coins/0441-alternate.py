class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Strategy:
        #   Use binary search to the find the greatest triangular number <= n.
        #   The index of this number in the list of all triangular numbers is the result.

        lo = 1
        hi = int(math.sqrt(n * 2))

        while lo <= hi:
            mid = (lo + hi) // 2
            x = mid * (mid + 1) // 2
            # Compare the <mid>th triangular number (with value <x>) with <n>
            if x == n:
                # <n> needs precisely <mid> columns
                return mid
            elif x < n:
                # <n> fills <mid> columns fully and needs at least one more column
                lo = mid + 1
            else:
                # <n> doesn't full all <mid> columns fully
                hi = mid - 1

        return hi
