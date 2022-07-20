a = [list(input().split()) for i in range(5)]

x = 0
y = 0
for i in range(5):
    for j in range(5):
        if a[i][j] == '1':
            x = i+1
            y = j+1

            break

print(abs(x-3) + abs(y-3))
