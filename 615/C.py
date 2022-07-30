from math import sqrt
for _ in range(int(input())):
    n = int(input())
    ans = []
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            if len(ans) == 0:
                ans.append(i)
                n /= i
            elif i != ans[0] and n/i != ans[0] and i != n/i:
                ans.append(i)
                ans.append(int(n/i))
                break

    if len(ans) == 3:
        print('YES')
        print(*ans)
    else:
        print('NO')
