for _ in range(int(input())):

    a = input()
    a = [int(i) for i in a]

    one = -1
    two = -1
    three = -1

    ans = 200000
    for i in range(len(a)):
        if a[i] == 1:
            one = i
        elif a[i] == 2:
            two = i
        else:
            three = i

        if one != -1 and two != -1 and three != -1:
            ans = min(ans, (max(one, two, three)-min(one, two, three)+1))

    if one == -1 or two == -1 or three == -1:
        print(0)
    else:
        print(ans)
