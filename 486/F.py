a, n, m = map(int, input().split())

seq = [0 for i in range(a+1)]

last = -1
for i in range(n):
    x, y = map(int, input().split())
    last = max(last, y)
    seq[x:y+1] = [1 for i in range(y-x+1)]

umb = {}
sol = [[float('inf') for i in range(a+1)] for i in range(m)]
for i in range(m):
    x, y = map(int, input().split())
