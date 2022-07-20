for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split(' ')))

    if len(a) % 2 != 0:
        print('NO')

    else:
        a = sorted(a)
        mid = int(n/2)
        flag = False
        ans = []
        for i in range(mid):
            if a[i] >= a[i+mid]:
                flag = True
                break
            else:
                if ans:
                    if ans[-1] <= a[i]:
                        flag = True
                        break
                ans.append(a[i])
                ans.append(a[i+mid])

        if flag:
            print('NO')
        else:
            print('YES')
            print(*ans)
