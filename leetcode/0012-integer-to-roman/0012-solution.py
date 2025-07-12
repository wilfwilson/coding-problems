class Solution:
    def intToRoman(self, num: int) -> str:
        out = ""
        n = str(num).zfill(4)
         
        # Deal with thousands digit
        out += int(n[0]) * 'M'

        # Deal with hundreds digit
        hundreds = n[1]
        if hundreds == '9':
            out += 'CM'
        elif hundreds == '4':
            out += 'CD'
        else:
            if int(hundreds) >= 5:
                out += 'D'
                hundreds = str(int(hundreds) - 5)
            if hundreds != '0':
                out += int(hundreds) * 'C'

        # Deal with tens digit
        tens = n[2]
        if tens == '9':
            out += 'XC'
        elif tens == '4':
            out += 'XL'
        else:
            if int(tens) >= 5:
                out += 'L'
                tens = str(int(tens) - 5)
            if tens != '0':
                out += int(tens) * 'X'

        # Deal with units digit
        units = n[3]
        if units == '9':
            out += 'IX'
        elif units == '4':
            out += 'IV'
        else:
            if int(units) >= 5:
                out += 'V'
                units = str(int(units) - 5)
            if units != '0':
                out += int(units) * 'I'

        return out
