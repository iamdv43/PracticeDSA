def countPairs(height, resistance):
    match = 0
    for i in height:
        if height.count(i) > 1:
            match += 1
        while i >= 1:
            i = i / ( resistance )
            if i in height:
                match += 1
    return match


height = [25, 1, 5, 7]
resistance = 5
print('Case 1: Output is ', countPairs(height, resistance))

height = [1,2,4,3,6]
resistance = 2
print('Case 2: Output is ', countPairs(height, resistance))
