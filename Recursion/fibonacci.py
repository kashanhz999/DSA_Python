# 0 1 1 2 3 5 8 13 21 34....
#write a fucntion that gives nth fibbonacci number
#f(3) => 2
#f(4) => 3

def fib(n):
  if n<=1:
    return n
  return fib(n-1)+fib(n-2)


if __name__ == '__main__':
  n = int(input())
  nth = fib(n)
  print(nth)