n = int(input())
a = input()
a = [i for i in a]
ans = 0
if n == 1:
    pass
elif n == 2:
    if a[0] == a[1]:
        ans += 1
        if a[0] == 'R':
            a[1] = 'G'
        else:
            a[1] = 'R'
else:
    a1 = a[0]
    a2 = a[1]
    for i in range(2, n):
        if a1 == a2:
            if a1 == 'R' and a[i] == 'R':
                a[i-1] = 'G'
            elif a1 == 'G' and a[i] == 'G':
                a[i-1] = 'R'
            elif a1 == 'B' and a[i] == 'B':
                a[i-1] = 'G'
            elif a1 == 'R' and a[i] == 'B':
                a[i-1] = 'G'
            elif a1 == 'B' and a[i] == 'R':
                a[i-1] = 'G'
            elif a1 == 'R' and a[i] == 'G':
                a[i-1] = 'B'
            elif a1 == 'G' and a[i] == 'R':
                a[i-1] = 'B'
            elif a1 == 'G' and a[i] == 'B':
                a[i-1] = 'R'
            elif a1 == 'B' and a[i] == 'G':
                a[i-1] = 'R'

            ans += 1

        a1 = a[i-1]
        a2 = a[i]

    if a[-2] == a[-1]:
        if a[-2] == 'R' and a[-3] == 'R':
            a[-2] = 'G'
        elif a[-2] == 'G' and a[-3] == 'G':
            a[-2] = 'R'
        elif a[-2] == 'B' and a[-3] == 'B':
            a[-2] = 'G'
        elif a[-2] == 'R' and a[-3] == 'B':
            a[-2] = 'G'
        elif a[-2] == 'B' and a[-3] == 'R':
            a[-1] = 'G'
        elif a[-2] == 'R' and a[-3] == 'G':
            a[-2] = 'B'
        elif a[-2] == 'G' and a[-3] == 'R':
            a[-2] = 'B'
        elif a[-2] == 'G' and a[-3] == 'B':
            a[-2] = 'R'
        elif a[-2] == 'B' and a[-3] == 'G':
            a[-2] = 'R'

        ans += 1

print(ans)
for i in a:
    print(i, end='')
print('')
