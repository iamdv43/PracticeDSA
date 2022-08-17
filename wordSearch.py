def exist( board, word):
    if not board:
        return False
    
    def dfs( i, j, word):
        if len(word) == 0: # all the characters are checked
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian 
        # check whether can find "word" along one direction
        res = dfs( i+1, j, word[1:]) or dfs( i-1, j, word[1:]) \
        or dfs( i, j+1, word[1:]) or dfs(i, j-1, word[1:])
        board[i][j] = tmp
        return res
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(i, j, word):
                return True      
    
    return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print("Ans: ",exist(board, word))
   