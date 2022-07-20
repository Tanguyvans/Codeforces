n = input()
m = int(n)
n = [int(i) for i in n]

ans = (m - 10**(len(n)-1)+1) * len(n)

for i in range(len(n)-1, 0, -1):
    ans += (10**i - 10**(i-1))*i

print(ans)
