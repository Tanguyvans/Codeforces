for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)

    even = 0
    odd = 0
    par = 0
    for i in range(n):
        if a[i] % 2 == 0:
            even += 1
        else:
            odd += 1

        if i < n-1:
            if a[i]+1 == a[i+1]:
                par += 1

    if even % 2 == 0 and odd % 2 == 0:
        print('YES')
    elif par != 0:
        print('YES')
    else:
        print('NO')
