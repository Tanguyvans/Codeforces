def find(c, a):
    if seq[c][a] == -1:
        return a
    else:
        return find(c, seq[c][a])


def union(c, a, b):

    s1 = find(c, a)
    s2 = find(c, b)

    if s1 != s2:
        seq[c][s2] = s1


n, m = map(int, input().split())

seq = [[-1 for i in range(n)] for i in range(m)]

for i in range(m):
    a, b, c = map(int, input().split())
    union(c-1, a-1, b-1)

q = int(input())
for i in range(q):
    count = 0
    a, b = map(int, input().split())
    for j in range(m):
        s1 = find(j, a-1)
        s2 = find(j, b-1)

        if s1 == s2:
            count += 1

    print(count)
