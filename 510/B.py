n = int(input())

sol = [[float('inf') for j in range(8)] for i in range(n+1)]

sol[0][0] = 0
for i in range(n):
    cost, vitamins = map(str, input().split())
    cost = int(cost)
    mask = 0
    for j in vitamins:
        if j == 'A':
            mask += 1
        elif j == 'B':
            mask += 2
        else:
            mask += 4

    for j in range(8):
        sol[i+1][j] = min(sol[i+1][j], sol[i][j])
        sol[i+1][(j | mask)] = min(sol[i+1][(j | mask)], sol[i][j]+cost)


ans = sol[-1][7]

if ans == float('inf'):
    print(-1)
else:
    print(ans)
