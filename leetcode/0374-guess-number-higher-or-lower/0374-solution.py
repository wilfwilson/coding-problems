# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        MAXINT = 2147483647
        lo = 1
        hi = MAXINT
        while hi - lo > 1:
            # Warning: would be an overflow in C++
            mid = (hi + lo) // 2
            x = guess(mid)
            if x == -1:
                hi = mid - 1
            elif x == 1:
                lo = mid + 1
            else:
                return mid
        
        if guess(lo) == 0:
            return lo
        else:
            return hi
