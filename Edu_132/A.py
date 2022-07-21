for _ in range(int(input())):
    x = int(input())
    doors = list(map(int, input().split()))

    while x != 0:
        inter = doors[x-1]
        doors[x-1] = 0
        x = inter

    imp = False
    for i in range(3):
        if doors[i] != 0:
            imp = True
            break

    if imp:
        print('NO')
    else:
        print('YES')
