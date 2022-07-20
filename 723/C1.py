n = int(input())
a = list(map(int, input().split()))

sol = [[0, 0] for i in range(n+1)]

pos = 0
nb_pos = 0
for i in range(n):

    if a[i] >= 0:
        pos += a[i]
        nb_pos += 1
        sol[i+1] = sol[i][:]

    else:
        ans = 0
        sol[i+1] = sol[i][:]
        for j in range(i+1):
            potions = sol[j][0]+1
            health = sol[j][1]+a[i]

            if health >= 0:
                if potions == sol[i+1][0]:
                    sol[i+1][1] = max(health, sol[i+1][1])
                elif potions > sol[i+1][0]:
                    sol[i+1] = [potions, health]

print(sol)
