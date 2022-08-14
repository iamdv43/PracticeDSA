def romanToInt(s):
    romans = {"I":1, "IV":4 ,"V":5, "IX":9 ,"X":10, "XL":40 ,
            "L":50, "XC":90 ,"C":100, "CD":400,"D":500, "CM":900,"M":1000}
    num = 0
    x = 0
    while x < len(s):
        if s[x:x+2] in romans.keys():
            num += romans[s[x:x+2]]
            x += 1
        else:
            num += romans[s[x]]
        x += 1
    return num

print("Ans: ", romanToInt("MCMXCIV"))