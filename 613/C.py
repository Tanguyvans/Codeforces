import math
n = int(input())

seq = [[] for i in range(int(math.sqrt(n))+1)]
seq[1] = 1
for i in range(2, int(math.sqrt(n))+1):
    if not seq[i]:
        for j in range(i, int(math.sqrt(n))+1, i):
            seq[j].append(i)
a = 1
b = n
for i in range(2, int(math.sqrt(n))+1):
    if n % i == 0:
        if max(a, b) >= max(i, n//i):
            imp = False
            for prime in seq[i]:
                if n//i % prime == 0:
                    imp = True

            if not imp:
                a = i
                b = n//i
print(a, b)
