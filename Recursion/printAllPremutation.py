'''
print all the permutation of a given array.

'''

# def recurPermute(arr,ds,res,mapi):
#   if len(ds)==len(arr):
#     res.append(ds)
    

#   for i in range(0,len(arr)):
#     if not mapi[i]:
#       ds = ds+[arr[i]]
#       mapi[i] = 1
#       recurPermute(arr,ds,res,mapi)
#       mapi[i] = 0
#       ds.pop()
   
      

# arr = [1,2,3]
# res = []
# mapi = [0]*len(arr)
# recurPermute(arr,[],res,mapi)
# print(res)

#Using BackTracking

def permute(arr,s,e):
  if s == e:
    print(arr)
  else:
    for i in range(s,e):
      arr[s],arr[i] = arr[i],arr[s]
      permute(arr,s+1,e)
      arr[s],arr[i] = arr[i],arr[s]

arr = [1,2,3]
n=  len(arr)
permute(arr,0,n)
      
      
