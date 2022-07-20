n = int(input())

a = list(map(int, input().split()))

l = [1] * 10**6
l[0] = 0
l[1] = 0
sol = set()
for i in range(len(l)):
    if l[i] == 1:
        for j in range(i*i, 10**12, i):
            if j == i*i:
                sol.add(j)
            if j < len(l):
                l[j] = 0
            else:
                break


for i in range(n):
    if a[i] in sol:
        print('YES')
    else:
        print('NO')
