
def find(i):
    if users[i] == -1:
        return i
    else:
        return find(users[i])


n, m = map(int, input().split())

users = {i: -1 for i in range(1, n+1)}
ntw = {i: 1 for i in range(1, n+1)}

for i in range(m):
    k = list(map(int, input().split()))
    nb = k[0]
    if len(k) > 1:
        s1 = find(k[1])
    for j in range(2, nb+1):
        s2 = find(k[j])

        if s1 != s2:
            users[max(s1, s2)] = min(s1, s2)
            ntw[min(s1, s2)] = ntw[s1] + ntw[s2]

            s1 = min(s1, s2)

for i in range(1, n+1):
    if users[i] == -1:
        print(ntw[i], end=' ')
    else:
        pos = users[i]
        ntw[i] = ntw[pos]
        print(ntw[i], end=' ')
