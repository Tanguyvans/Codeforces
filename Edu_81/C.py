for _ in range(int(input())):
    s = list(input())
    t = list(input())

    imp = False
    for i in t:
        if i not in s:
            imp = True

    if imp:
        print(-1)
        continue

    seq = {}
    for cnt, si in enumerate(s):
        if si not in seq:
            seq[si] = [cnt]
        else:
            seq[si].append(cnt)

    i = 0
    ans = 1
    pt = -1
    for ti in t:
        found = False
        for i in seq[ti]:
            if pt < i:
                found = True
                pt = i
                break

        if not found:
            pt = seq[ti][0]
            ans += 1

    print(ans)
