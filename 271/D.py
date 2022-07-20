t, k = map(int, input().split())

p = 10**9+7
dp = [i for i in range(1, k+1)]

for i in range(k, 10**5+10):
    dp += [(dp[i-1]+dp[i-k]+1) % p]

for _ in range(t):
    a, b = map(int, input().split())
    print((dp[b]-dp[a-1]) % p)
