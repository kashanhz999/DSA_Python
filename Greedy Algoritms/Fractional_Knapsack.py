class Item:
  def __init__(self,value,weight):
    self.value = value
    self.weight = weight
    
def fractionalKnapsack(w,arr):
  arr.sort(key = lambda x:(x.value/x.weight),reverse=True)
  finalVal = 0.0
  for i in arr:
    if i.weight <=w:
      w-=i.weight
      finalVal+=i.value
    else:
      finalVal += i.value * w / i.weight
      break
  print(finalVal)
      
if __name__ == '__main__':
  w = 50
  val = [60,100,120]
  weight = [10,20,30]
  n = len(val)
  zipper= []
  for i in range(n):
    zipper.append(Item(val[i],weight[i]))
  fractionalKnapsack(w,zipper)