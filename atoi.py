def myAtoi(s: str) -> int:
    s = s.strip()
    pos, value, sign = 1, 0, 1 
    c = s[0] if len(s) > 0 else "break"
    if c == "-" or c == "+":
            sign = -1 if c == "-" else 1
    else: 
        if c.isdigit():
            value = value*10 + int(c) 
        else:
            pos = len(s)
    while pos < len(s):
        c = s[pos]
        if c.isdigit():
            value = value*10 + int(c)
        else:
            break 
        pos = pos + 1 
    value = sign * value
    if value > (2 ** 31)-1:
        value = min(value, (2 ** 31)-1)
    if value < -(2 ** 31):
        value = max(-(2 ** 31), value)
    return value

print("Ans: ", myAtoi("   -42"))