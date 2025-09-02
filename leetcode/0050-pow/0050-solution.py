class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1

        binary = str(bin(abs(n)))[:1:-1]
        if binary[0] == '0':
            out = 1.0
        else:
            out = x

        power = x
        for i in range(1, math.floor(math.log2(abs(n))) + 1):
            power = power * power # power = x ^ (2 ^ i)
            if binary[i] == '1':
                out *= power

        if n < 0:
            out = 1 / out

        return out
