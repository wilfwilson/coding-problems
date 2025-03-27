class Solution:
    # quick string method is: return str(x) == str(x)[::-1]

    # Func to determine whether an int equals its reverse (including its sign)
    def isPalindrome(self, x: int) -> bool:
        import math

        if x < 0:
            return False

        nrDigits = math.ceil(math.log10(x + 1))
        digits = []
        for i in range(nrDigits):
            y = x % 10
            digits.append(y)
            x = (x - y) / 10

        for i in range(int(nrDigits / 2)):
            if digits[i] != digits[nrDigits - i - 1]:
                return False

        return True
