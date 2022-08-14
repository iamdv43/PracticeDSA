def rotateimage(matrix):
    n = len(matrix)
        
    i = 0 # index for row
    for k in range(n-1, -1, -2):
        for j,x in enumerate(matrix[i][i:i+k],i): # j: index for col
            a, b = j-i, k-(j-i) # (a, b) is the difference vector
            matrix[i][j], matrix[i+a][j+b], matrix[i+a+b][j-a+b], matrix[i+b][j-a] = matrix[i+b][j-a], matrix[i][j], matrix[i+a][j+b], matrix[i+a+b][j-a+b] # rotate
        i += 1

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
rotateimage(matrix)
print("Ans: ",  matrix)