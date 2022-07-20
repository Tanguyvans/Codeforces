n = int(input())

a = list(map(int, input().split(' ')))

b0 = 0
b = [0 for i in range(n)]
for i in range(n):
    b[i] = a[i]+b0
    b0 = b[i]

if b[-1]/3 == 0:
    sol = b.count(0)
    print(int(1/2*(sol-1)*(sol-2)))
elif int(b[-1]/3) != b[-1]/3:
    print(0)
elif n < 3:
    print(0)
else:
    b1 = 0
    b2 = 0
    for i in range(n):
        if b2 == 0 and b[i]*3 == b[-1]:
            b1 += 1
        elif b1 > 0 and b[i]*3/2 == b[-1]:
            b2 += 1
        elif b2 > 0 and b[i]*3 == b[-1]:
            b2 += 1

    print(b1*b2)
