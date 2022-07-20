import math

n, m = map(int, input().split())

kmax = (n-m)*(n-m+1)//2

kmin = (n % m) * (n//m) * (n//m+1) // 2 + (m-n % m) * (n//m) * (n//m-1) // 2
print(kmin, kmax)
