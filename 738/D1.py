def find(p, a):

    if seq[p][a] == -1:
        return a
    else:
        return find(p, seq[p][a])


n, m1, m2 = map(int, input().split())

seq = [[-1 for i in range(n)] for i in range(2)]

for i in range(m1):
    a, b = map(int, input().split())
    s1 = find(0, a-1)
    s2 = find(0, b-1)
    seq[0][s2] = s1

for i in range(m2):
    a, b = map(int, input().split())

    s1 = find(1, a-1)
    s2 = find(1, b-1)
    seq[1][s2] = s1

ans = 0
sol = []
for i in range(n):
    s11 = find(0, i)
    s21 = find(1, i)
    for j in range(i+1, n):

        s12 = find(0, j)
        s22 = find(1, j)

        if s11 != s12 and s21 != s22:
            ans += 1
            seq[0][s12] = s11
            seq[1][s22] = s21

            sol.append((i+1, j+1))

print(ans)
for i in range(ans):
    print(sol[i][0], sol[i][1])
