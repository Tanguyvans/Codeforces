sol = [0 for i in range(1100)]
sol[0] = 1

for i in range(11, 1100):
    if sol[i-11] == 1:
        sol[i] = 1
    if i >= 111:
        if sol[i-111] == 1:
            sol[i] = 1

for _ in range(int(input())):
    a = int(input())
    if a >= 1100:
        print('YES')
    elif sol[a] == 1:
        print('YES')
    else:
        print('NO')
