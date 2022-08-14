def intToRoman(num):
    data = {1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",50:"L",40:"XL",10:"X",9:"IX",5:"V",4:"IV",3:"III", 2:"II", 1:"I"}
        
    ans = "" 
    tmp =""
    for i, v in data.items(): 
        while num>=i:  
            if num in data: 
                ans += data[num]
                num -= i
            else: 
                tmp += v 
                num -= i
        ans +=tmp
        tmp =""

    return ans

print(intToRoman(3))
print(intToRoman(58))
print(intToRoman(1994))