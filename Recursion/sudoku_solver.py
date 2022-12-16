'''
A sudoku board is a 9X9 board which is comprised of 9 3X3 boards, to solve a sudoku puzzle we have to follow certain rules.
Rules:
1. The digit 1 to 9 should exactly appear once in every row
2. The digit 1 to 9 should exactly appear once in every col
3. The digit 1 to 9 should exactly appear once in every  
   3X3.
   
'''

#check if the number can be placed at that point in the matrix.
def isValid(grid,row,col,tar):
  for i in range(9):
    if grid[i][col] == tar:
      return False
    if grid[row][i] == tar:
      return False
    #the expression (3 * (row / 3) + i / 3) evaluates to the row numbers of that 3×3 submatrix and the expression (3 * (col / 3) + i % 3) evaluates to the    
    #column numbers.
    if grid[3*(row//3)+i//3][3*(col//3)+i%3] == tar:
      return False
  return True


def solveSudoku(grid):
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == 0:
        for c in range(1,10):
          if isValid(grid,i,j,c):
            grid[i][j] = c

            if solveSudoku(grid):
              return True
            else:
              grid[i][j]=0
        return False
  return True

if __name__ == '__main__':
  grid = [[0 for _ in range(9)] for _ in range(9)]
  
  grid = [[9,5,7,0,1,3,0,8,4],[4,8,3,0,5,7,1,0,6],[0,1,2,0,4,9,5,3,7],[1,7,0,3,0,4,9,0,2],[5,0,4,9,7,0,3,6,0],[3,0,9,5,0,8,7,0,1],[8,4,5,7,9,0,6,1,3],      
         [0,9,1,0,3,6,0,7,5],[7,0,6,1,8,5,4,0,9]]
  
  solveSudoku(grid)
  print(grid)