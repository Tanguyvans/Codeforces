

def func(nb):
    if nb in seq:
        return seq[nb]
    else:
        if int(nb) % 8 == 0:
            seq[nb] = [True, nb]
            return seq[nb]
        else:
            ans = False
            sol = -1
            for i in range(len(nb)):
                s = nb[:i]
                s += nb[i+1:] if i < len(nb)-1 else ''
                if s:
                    ma, ms = func(s)
                    if ma:
                        ans = True
                        sol = ms
                        break

            if sol:
                seq[nb] = [ans, sol]
            else:
                seq[nb] = [ans, sol]

            return seq[nb]


x = input()

seq = {}

ans, sol = func(x)

if ans:
    print('YES')
    print(sol)
else:
    print('NO')
