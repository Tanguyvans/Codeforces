def solve():
    n, k = map(int, input().split())

    if k >= 2 and n % 2 == 1:
        print("NO")
    else:
        print("YES")

        for i in range(1, n+1):
            print(*[i for i in range(i, n*k+1, n)])


for _ in range(int(input())):
    solve()
