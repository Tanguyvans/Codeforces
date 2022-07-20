
n, t = map(int, input().split(' '))

a = list(map(int, input().split(' ')))

ans = 0
somme = 0
j = 0
flag = False
for i in range(n):
    while somme + a[j] <= t:
        somme += a[j]
        j += 1
        ans = max(ans, j-i)
        if j == n:
            flag = True
            break

    if flag:
        break

    somme -= a[i]

print(ans)
