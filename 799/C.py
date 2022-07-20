n = 7
for _ in range(int(input())):
    h = 0
    input()
    for i in range(n):
        a = input()
        x = 0
        l = 0
        for j in range(n):
            if a[j] == '#':
                x += 1
                h = i
                l = j

        if x == 1:
            break

    print(h, l)
