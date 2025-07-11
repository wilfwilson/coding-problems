class Solution:
    def reverse(self, x: int) -> int:
        max_lim = 2147483647
        min_lim = 2147483648

        if x < 0:
            s = str(x)[:0:-1]
            sign = '-'
            lim = str(min_lim)
        else:
            s = str(x)[::-1]
            sign = ''
            lim = str(max_lim)

        if len(s) < 10:
            return int(sign + s)
   
        for i in range(10):
            if s[i] < lim[i]:
                return int(sign + s)
            elif s[i] > lim[i]:
                return 0

        return int(sign + s) # s = lim
