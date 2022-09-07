n, m, q = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

k = list(map(int, input().split()))

for i in range(q):
    ki = k[i]

    ai = sorted(a, reverse=True)
    bi = sorted(b, reverse=True)

    seq = []
