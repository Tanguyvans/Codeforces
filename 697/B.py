sol = [False for i in range(10**7)]
sol[2020] = True
sol[2021] = True
for i in range(2020, 10**7):
    if sol[i]:
        if i+2020 < 10**7:
            sol[i+2020] = True
        if i+2021 < 10**7:
            sol[i+2021] = True

for _ in range(int(input())):
    n = int(input())

    if sol[n]:
        print('YES')
    else:
        print('NO')
