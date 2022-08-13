def find(a):
    if seq[a] == -1:
        return a
    else:
        return find(seq[a])


n = int(input())
seq = [-1 for i in range(n)]

closed = []
ans = 0
for i in range(n-1):
    a, b = map(int, input().split())
    s1 = find(a-1)
    s2 = find(b-1)

    if s1 == s2:
        closed.append((a-1, b-1))
        ans += 1
    else:
        seq[s2] = s1

print(ans)
for i in range(len(seq)):
    s1 = find(i)
    for j in range(i+1, len(seq)):
        s2 = find(j)
        if s2 != s1:
            seq[s2] = s1

            c1, c2 = closed.pop()
            print(c1+1, c2+1, i+1, j+1)
