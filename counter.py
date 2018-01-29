import time

def sumOfN2(n):
   start = time.time()

   Sum = 0
   for i in range(1,n+1):
      Sum = Sum + i

   end = time.time()

   return Sum,end-start
