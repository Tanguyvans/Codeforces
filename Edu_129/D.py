
def solve(n, x, dp):
    if len(str(x)) >= n:
        return 0

    if x in dp:
        return dp[x]

    ans = float('inf')

    for i in str(x):
        if i != '1' and i != '0':
            ans = min(ans, 1+solve(n, x*int(i), dp))
            dp[x] = ans
    return ans


n, x = map(int, input().split(' '))
dp = {}

sol = solve(n, x, dp)
print(-1 if sol == float('inf') else sol)
