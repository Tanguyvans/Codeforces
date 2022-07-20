import math
n = int(input())
ans = math.factorial(n)
ans //= 2

ans //= (n//2)**2

print(ans)
