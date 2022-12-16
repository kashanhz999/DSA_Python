def solve(i,j,a,n,ans,move,vis):
  if i==n-1 and j==n-1:
    ans.append(move)
    return
  
  # downward Movement
  if i+1<n and not vis[i+1][j] and a[i+1][j]==1:
    vis[i][j] =1
    solve(i+1,j,a,n,ans,move+'D',vis)
    vis[i][j] = 0
  # left movement
  if j-1>=0 and not vis[i][j-1] and a[i][j-1] ==1:
    vis[i][j]  =1
    solve(i,j-1,a,n,ans,move+'L',vis)
    vis[i][j] = 0
  #right Movement
  if j+1<n and not vis[i][j+1] and a[i][j+1] ==1:
    vis[i][j]= 1
    solve(i,j+1,a,n,ans,move+'R',vis)
    vis[i][j]=0
  #upward Movement
  if i-1 >=0 and not vis[i-1][j] and a[i-1][j] ==1:
    vis[i][j] = 1
    solve(i-1,j,a,n,ans,move+'U',vis)
    vis[i][j] = 0

if __name__ == '__main__':
  n = 4
  matrix = [[0 for _ in range(n)] for _ in range(n)]
  matrix = [[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]]
  ans = []
  vis = [[0 for _ in range(n)] for _ in range(n)]
  if matrix[0][0] == 1:
    solve(0,0,matrix,n,ans,"",vis)
  print(ans)
  