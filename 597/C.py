l = input()
if 'm' in l:
    print(0)
elif 'w' in l:
    print(0)
else:

    a = [i for i in l]
    dp = [1 for i in range(len(a)+2)]
    dp[0] = 1
    dp[1] = 1

    p = 10**9+7

    for i in range(2, len(a)+1):
        dp[i] = dp[i-1]
        if a[i-1] == a[i-2] and (a[i-1] == 'u' or a[i-1] == 'n'):
            dp[i] = (dp[i] + dp[i-2]) % p

    print(dp[len(a)])
