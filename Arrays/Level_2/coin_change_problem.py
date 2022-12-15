def minimum(coin_arr,amt):
  dp = [0 for _ in range(amt+1)]
  dp[0] = 1
  for i in range(len(coin_arr)):
    for j in range(coin_arr[i],len(dp)):
      dp[j] += dp[j - coin_arr[i]]
  return dp[amt]
if __name__ == '__main__':
  coin_arr = list(map(int,input().split()))
  amt = int(input())
  print(minimum(coin_arr,amt))
  