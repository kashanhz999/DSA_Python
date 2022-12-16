def find_minimum_coins(coins,v):
  n = len(coins)
  ans = []
  for i in range(n-1,-1,-1):
    while v >=coins[i]:
      v -= coins[i]
      ans.append(coins[i])
  print(ans)



if __name__ == '__main__':
  v = 49
  coins = [1,2,5,10,20,50,100,500,100]
  find_minimum_coins(coins,v)
  