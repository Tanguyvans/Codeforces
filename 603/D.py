from hashlib import new


n = int(input())

sol = []
for i in range(n):
    word = set(input())

    new_sol = []
    for s in sol:
        if word.intersection(s):
            word = word.union(s)
        else:
            new_sol.append(s)
    new_sol.append(word)

    sol = new_sol[:]

print(len(new_sol))
