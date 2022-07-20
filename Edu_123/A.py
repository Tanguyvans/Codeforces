
for _ in range(int(input())):

    passage = input()

    check_keys = ['r', 'g', 'b']
    keys = []
    doors = []
    flag = False
    for i in passage:
        if i in check_keys:
            keys.append(i)

        elif i.lower() not in keys:
            flag = True
            break

    if flag:
        print('NO')
    else:
        print('YES')
