def zigzagconvert(s: str, numRows: int) -> str:

        length = len(s)
        if numRows == 1 or length <= numRows:
            return s

        if numRows == 2:
            return s[::2] + s[1::2]

        if numRows == 3:
            return s[::4] + s[1::2] + s[2::4]

        dist = 2 * numRows - 2
        start = s[::dist]
        end = s[numRows-1::dist]
        middle = ""
        for i in range(1, numRows - 1):
            j = i
            d2 = 2 * i
            d1 = dist - d2
            while j < length:
                middle += s[j]
                j += d1
                d1, d2 = d2, d1

        return start + middle + end

s = "PAYPALISHIRING"
n = 4
print(zigzagconvert(s, n))