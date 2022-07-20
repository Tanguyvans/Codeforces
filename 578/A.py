n = int(input())

a = input()
a = [i for i in a]

ans = [0 for i in range(10)]

for i in range(n):
    if a[i] == 'L':
        for j in range(10):
            if ans[j] == 0:
                ans[j] = 1
                break

    elif a[i] == 'R':
        for j in range(9, -1, -1):
            if ans[j] == 0:
                ans[j] = 1
                break

    else:
        ans[int(a[i])] = 0

for i in range(10):
    print(ans[i], end='')

print('')
