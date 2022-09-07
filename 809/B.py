for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    s1 = [[0, 0] for i in range(n)]
    s2 = [[0, 0] for i in range(n)]
    for i in range(n):

        if s1[a[i]-1][0] == 0 and s1[a[i]-1][1] == 0:
            s1[a[i]-1][0] += 1
            s1[a[i]-1][1] = i
        elif s1[a[i]-1][0] != 0 and s1[a[i]-1][1] % 2 != i % 2:
            s1[a[i]-1][0] += 1
            s1[a[i]-1][1] = i
        elif s2[a[i]-1][0] == 0 and s2[a[i]-1][1] == 0:
            s2[a[i]-1][0] += 1
            s2[a[i]-1][1] = i
        elif s2[a[i]-1][0] != 0 and s2[a[i]-1][1] % 2 != i % 2:
            s2[a[i]-1][0] += 1
            s2[a[i]-1][1] = i

    for i in range(n):
        print(max(s1[i][0], s2[i][0]), end=' ')

    print()
