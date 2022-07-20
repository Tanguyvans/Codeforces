import math

s1 = input()
s2 = input()

p1 = 0
n1 = 0

p2 = 0
n2 = 0
d2 = 0

for i in range(len(s1)):
    if s1[i] == '+':
        p1 += 1
    elif s1[i] == '-':
        n1 += 1

    if s2[i] == '+':
        p2 += 1
    elif s2[i] == '-':
        n2 += 1
    else:
        d2 += 1

final = p1 - n1
pos = p2 - n2

if final == pos and d2 == 0:
    print(1)
elif abs(final-pos) > d2 or (max(d2, abs(final-pos)) - min(d2, abs(final-pos))) % 2 != 0:
    print(0)
else:
    num = 1
    r = (d2 - abs(final - pos))//2
    for i in range(d2, r, -1):
        num *= i
    ans = num/math.factorial(d2-r)

    print(ans * (1/2) ** d2)
