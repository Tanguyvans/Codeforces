from collections import deque as dq

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


for _ in range(int(input())):
    a = input()
    a = [i for i in a]
    g = {alphabet[i]: [] for i in range(26)}

    for i in range(len(a)-1):
        if a[i] not in g[a[i+1]]:
            g[a[i+1]].append(a[i])

        if a[i+1] not in g[a[i]]:
            g[a[i]].append(a[i+1])

    vis = {alphabet[i]: 100 for i in range(26)}
    d = dq()
    d.append([a[0], 0, True])
    vis[a[0]] = 0
    possible = True
    pos = True
    center = a[0]
    while(len(d)) > 0:
        letter, nb, up = d.popleft()
        if len(g[letter]) > 2:
            possible = False
            break
        for k in g[letter]:
            if vis[k] == 100:
                if up:
                    if nb+1 not in vis.values():
                        vis[k] = nb + 1
                        add = 1
                    elif nb-1 not in vis.values() and letter == center:
                        vis[k] = nb - 1
                        up = False
                        add = -1
                    else:
                        possible = False
                else:
                    if nb-1 not in vis.values():
                        vis[k] = nb - 1
                        add = -1
                    else:
                        possible = False
                d.append([k, nb+add, up])
            elif abs(vis[k]-nb) != 1:
                possible = False
                break

    if possible:
        print('YES')
        sol = {k: v for k, v in sorted(vis.items(), key=lambda item: item[1])}
        for k, v in sol.items():
            print(k, end='')
        print('')
    else:
        print('NO')
