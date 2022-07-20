for _ in range(int(input())):
    a, b, c, d = map(int, input().split(' '))

    s = input()

    if len(s) > 1:

        l = [a, b, c, d]
        r = l[:]

        fl = False
        fr = False
        pl = False
        pr = False
        for i in range(len(s)-1):

            if not pl:
                if l[2] > 0 and s[i] + s[i+1] == 'AB':
                    l[2] -= 1
                    pl = True
                elif l[3] > 0 and s[i] + s[i+1] == 'BA':
                    l[3] -= 1
                    pl = True
                elif l[0] > 0 and s[i] == 'A':
                    l[0] -= 1
                elif l[1] > 0 and s[i] == 'B':
                    l[1] -= 1
                else:
                    fl = True
            else:
                pl = False

            if not pr:
                if r[2] > 0 and s[-i-2] + s[-i-1] == 'AB':
                    r[2] -= 1
                    pr = True
                elif r[3] > 0 and s[-i-2] + s[-i-1] == 'BA':
                    r[3] -= 1
                    pr = True
                elif r[0] > 0 and s[i] == 'A':
                    r[0] -= 1
                elif r[1] > 0 and s[i] == 'B':
                    r[1] -= 1
                else:
                    fr = True
            else:
                pr = False

        if fr and fl:
            print('NO')
        else:
            print('YES')

    else:
        if (s == 'B' and b > 0) or (s == 'A' and a > 0):
            print('YES')
        else:
            print('NO')
