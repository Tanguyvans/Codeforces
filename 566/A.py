n = int(input())

if n % 2 != 0:
    ans = 0
else:
    ans = 2**(n//2)

print(ans)
