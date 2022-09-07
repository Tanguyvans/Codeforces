for _ in range(int(input())):
    a, s = map(str, input().split())

    j = len(s)-1
    b = ''
    imp = False
    for i in range(len(a)-1, -1, -1):
        if int(a[i]) > int(s[j]):
            if j >= 1:
                bi = int(s[j-1:j+1]) - int(a[i])
                if bi > 9 or bi < 0:
                    imp = True
                    break
                b = str(bi) + b
                j -= 2
            else:
                imp = True
                break
        else:
            if j >= 0:
                bi = int(s[j]) - int(a[i])
                if bi > 9 or bi < 0:
                    imp = True
                    break
                b = str(bi) + b
                j -= 1
            else:
                imp = True
                break

    if j >= 0:
        b = s[:j+1] + b

    if imp:
        print(-1)
    else:
        print(int(b))
