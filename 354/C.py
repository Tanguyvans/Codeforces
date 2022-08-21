n, k = map(int, input().split())

a = list(input())
seq = [0 for i in range(n)]

na = 0
nb = 0
for i in range(n):
    if a[i] == 'a':
        na += 1
    else:
        nb += 1

    if na == nb:
        seq[i] = na*2
    elif i % 2 == 0:
        seq[i] = seq[i-1]

print(seq)
