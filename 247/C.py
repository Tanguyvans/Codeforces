from collections import deque as dq
from math import factorial
n, k, d = map(int, input().split())


stack = dq()
stack.append([k, [], 0, False])

ans = 0
while len(stack) > 0:
    m, l, nb, isD = stack.popleft()
    for i in range(1, m+1):
        if nb + i < n:
            if isD or i >= d:
                a = l[:]
                a.append(i)
                stack.append([i, a, nb+i, True])
            else:
                a = l[:]
                a.append(i)
                stack.append([i, a, nb+i, False])
        elif nb + i == n:
            if isD or i >= d:
                a = l[:]
                a.append(i)
                print(a)
                ans += 1
            break
        else:
            break

print(ans)
