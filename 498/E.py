n, q = map(int, input().split())

sup = list(map(int, input().split()))
g = {i: [] for i in range(n)}

for i in range(n-1):
    g[sup[i]-1].append(i+1)
    # g[i+2].append(sup[i])

stack = []
stack.append(0)
seq = [[] for i in range(n)]
seq[0].append(1)
while len(stack) > 0:
    pos = stack[-1]
    if g[pos]:
        added = False
        for k in g[pos]:
            if seq[k] == []:
                stack.append(k)
                added = True
                for j in stack:
                    seq[j].append(k+1)
                break

        if not added:
            stack.pop()
    else:
        stack.pop()

# print(seq)

for i in range(q):
    start, end = map(int, input().split())

    if len(seq[start-1]) <= end-1:
        print(-1)
    else:
        print(seq[start-1][end-1])
