a = input()
a = [int(i) for i in a]

sol = [0 for i in range(9)]
for i in range(len(a)):
    for j in range(a[i]):
        sol[j] += 10**(len(a)-i-1)

for i in range(9):
    if sol[i] == 0:
        break

    nb = i

print(nb+1)
print(*sol[:nb+1])
