
def find(a):
    if seq[a] == -1:
        return a
    else:
        return find(seq[a])


n, m = map(int, input().split())

seq = [-1 for i in range(n)]

winner = 0
w = []
for i in range(m):
    l, r, x = map(int, input().split())

    for j in range(l-1, x):
        if seq[j] == -1 and j != x-1:
            seq[j] = x-1
            break
    for j in range(r-1, x-1, -1):
        if seq[j] == -1 and j != x-1:
            seq[j] = x-1
            break

    w.append(x-1)
    winner = x-1

w = {}
pointer = -1
print(seq)
for i in range(n):
    if seq[i] != -1:
        if seq[i] not in w:
            if pointer != -1:
                w[pointer] = seq[i]

        w[seq[i]] = -1
        pointer = seq[i]

        print(pointer+1, end=' ')
    elif seq[i] == -1 and i != winner:
        print(pointer, end=' ')
    else:
        print(0, end=' ')
