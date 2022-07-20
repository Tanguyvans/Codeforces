mod = [111111111, 11111111, 1111111, 1111111, 111111, 11111, 1111, 111, 11]
mod = sorted(mod)
n = 10**10
l = [0 for i in range(n)]
for i in mod:
    l[i] = 1
    for j in range(i, n):
        if l[j-i] == 1:
            l[j] = 1

print(l)
for _ in range(int(input())):
    a = int(input())

    for modi in mod:
        a = a % modi

    if a != 0:
        print('NO')
    else:
        print('YES')
