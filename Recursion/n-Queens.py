def isSafe1(row,col,board,N):
  for i in range(col):
        if board[row][i] == "Q":
            return False
          
  for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False
          
  for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False
 
  return True
  
  
    

def solve(col,board,n):
  if col == n:
    print(board)
  else:
    for row in range(0,n):
      if isSafe1(row,col,board,n):
        board[row][col] = 'Q'
        solve(col+1,board,n)
        board[row][col] = '.'
        
  
  

def solveNQueen(n):
  board = [["." for _ in range(n)] for _ in range(n)]
  solve(0,board,n)

if __name__ == '__main__':
  n =4    
  solveNQueen(n)
  
  
  
    
  
  
