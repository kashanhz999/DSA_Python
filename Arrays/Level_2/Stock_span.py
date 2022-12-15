def peek(st):
  if st:
    return st[-1]
  else:
    return None

def span(stock):
  span = [-1 for _ in range(len(stock))]
  st = []
  
  st.append(0)
  span[0] = 1
  
  for i in range(1,len(stock)):
    while(len(st)>0 and stock[i]> stock[peek(st)]):
      st.pop()
    if len(st) == 0:
      span[i] = i+1
    else:
      span[i] = i-peek(st)
    st.append(i)
  return span   
    
ar = [100 ,80 ,60 ,70 ,60, 75 ,85]
print(span(ar))
  