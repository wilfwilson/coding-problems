class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        if num1 == "0" or num2 == "0":
            return max(num1, num2)

        out = ""
        carry = 0

        i = len(num1)
        j = len(num2)

        while i > 0 or j > 0:
            i -= 1
            j -= 1

            x = int(num1[i]) if i >= 0 else 0
            y = int(num2[j]) if j >= 0 else 0
            
            temp = x + y + carry
            if temp > 9:
                carry = 1
                temp = temp - 10
            else:
                carry = 0

            out += str(temp)

        if carry == 1:
            out += "1"

        return out[::-1]
