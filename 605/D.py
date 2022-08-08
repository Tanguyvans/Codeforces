n = int(input())
a = list(map(int, input().split()))

seq = [0 for i in range(n)]
seq[0] = 1
for i in range(n-1):
    if a[i] < a[i+1]:
        seq[i+1] = seq[i] + 1
    else:
        seq[i+1] = 1

ans = 0
j = 0
lj = 0

k = 0
lk = 0

fj = False
fk = False
for i in range(1, n):
    ans = max(ans, seq[i])
    if seq[i] == 1:
        lj = seq[i-1] - 1
        j = i-2
        fj = False

        lk = seq[i-1]
        k = i-1
        fk = False

    if a[j] < a[i] and not fj:
        ans = max(ans, lj+seq[i])
    else:
        fj = True

    if i < n-1:
        if a[k] < a[i+1] and not fk:
            ans = max(ans, lk+seq[i+1]-1)
        else:
            fk = True

print(ans)
