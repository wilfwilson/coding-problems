def myAtoi(s):
    n = len(s)

    sign = "+"
    out = ""

    i = 0

    # Ignore leading whitespace
    while i < n and s[i] == " ":
        i += 1

    # Update the sign if given
    if i < n and (s[i] == "-" or s[i] == "+"):
        sign = s[i]
        i += 1

    # Ignore leading zeroes
    while i < n and s[i] == "0":
        i += 1
    
    # Read in at most 11 digits
    # Any number with 11 or more digits will be out of bounds and therefore get rounded,
    #   as may be the case for numbers with 10 digits
    while i < n and s[i].isdigit() and len(out) < 11:
        out += s[i]
        i += 1

    # No digits read in
    if len(out) == 0:
        return 0

    # Determine the appropriate bound to use
    if sign == "-":
        bound = "2147483648" # 2 ^ 31
    elif sign == "+":
        bound = "2147483647" # (2 ^ 31) - 1

    if len(out) == 11:
        out = bound
    elif len(out) == 10:
        # Find the first index, if any, where <out> and <bound> may differ
        for i in range(len(out)):
            if out[i] != bound[i]:
                break
      
        # Replace <out> by <bound> if
        if out[i] > bound[i]:
            out = bound

    return int(sign + out)
