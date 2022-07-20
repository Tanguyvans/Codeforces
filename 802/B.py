for _ in range(int(input())):
    n = int(input())
    a = input()

    ans = ''
    if int(a[0]) == 9:
        sol = str('1')*(n+1)
        ans = int(sol)-int(a)
    else:
        sol = str('9')*n
        ans = int(sol)-int(a)

    print(ans)
