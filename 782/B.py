for _ in range(int(input())):
    n, k = map(int, input().split(' '))
    ki = k
    seq = input()
    seq = [int(i) for i in seq]

    act = [0 for i in range(n)]

    ans = []
    for i in seq:
        if ki % 2 == 0 and i == 0:
            ans.append(0)
        elif ki % 2 != 0 and i != 0:
            ans.append(0)
        else:
            ans.append(1)

    i = 0
    while k > 0 and i < len(seq):

        if ki % 2 == 0:
            if seq[i] != 1:
                k -= 1
                act[i] += 1
            ans[i] = 1

        else:
            if seq[i] == 1:
                k -= 1
                act[i] += 1

            ans[i] = 1

        i += 1
    if k != 0:
        if k % 2 == 0:
            act[-1] += k
        else:
            act[-1] += k
            ans[-1] = 0 if ans[-1] == 1 else 0

    print(''.join([str(i) for i in ans]))
    print(*act)
