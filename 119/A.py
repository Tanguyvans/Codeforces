n, a, b, c = map(int, input().split(' '))

l = [0 for i in range(n)]

for i in [a, b, c]:
    if i <= n:
        l[i-1] = max(l[i-1], 1)

        if i < n:
            for j in range(i, n):
                if l[j-i] != 0:
                    l[j] = max(l[j], l[j-i]+1)

print(l[-1])
