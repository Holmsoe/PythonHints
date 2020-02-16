
import time
from math import sqrt

start = time.time()
print("hello")

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

def sumn(n):
    if n == 1:
        return 1
    else:
        return n + sumn(n-1)
print(sumn(5))

memo = {0:0, 1:1}
def fibm(n):
    if not n in memo:
        memo[n] = fibm(n-1) + fibm(n-2)
    return memo[n]
print(fibm(10))


end = time.time()
print(end - start)

memo1 = {1:1}
def minsum(n):
    if not n in memo1:
        memo1[n] = n + minsum(n-1)
    return memo1[n]
print(minsum(4))

memo2 = {0:0,1:1}
def minsumA(n):
    if not n in memo2:
        memo2[n] = n + minsumA(n-2)
    return memo2[n]
print(minsumA(6))



def primes(n):
    if n == 0:
        return []
    elif n == 1:
        return []
    else:
        p = primes(int(sqrt(n)))
        no_p = [j for i in p for j in range(i*2, n + 1, i)]
        p = [x for x in range(2, n + 1) if x not in no_p]
        return p


print(primes(10))


