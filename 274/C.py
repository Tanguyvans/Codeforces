n = int(input())
ab = []
for i in range(n):
    a, b = map(int, input().split(' '))
    ab.append([a, b])

ab = sorted(ab, key=lambda ab: (ab[0], ab[1]))

day = 0

for abi in ab:
    if day <= abi[1]:
        day = abi[1]
    else:
        day = abi[0]

print(day)
