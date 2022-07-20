power = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]

for _ in range(int(input())):
    n, k = map(int, input().split(' '))
    b = list(map(int, input().split(' ')))
    c = list(map(int, input().split(' ')))

    steps = [0 for i in range(10000000)]
    for i in range(len(b)):
        stp = 0
        for j in range(len(power)):
            if b[i] <= power[j]:
                stp = j
                break

        steps2 = steps[:]
        steps2[stp] = max(steps[stp], c[i])
        for j in range(len(steps)):
            if steps[j] != 0:
                steps2[j+stp] = max(steps2[j+stp], steps[j] + c[i])
            if j > k:
                break
        steps = steps2[:]

    print(steps[k])
