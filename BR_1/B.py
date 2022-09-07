import math

a1 = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
      'N': 14, '0': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}


a2 = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M',
      14: 'N', 15: '0', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}

for _ in range(int(input())):
    a = input()
    b = a
    a = [i for i in a]
    flag = False
    if len(a) < 4 or a[0] != 'R':
        flag = True
    else:
        flag = True
        for i in range(1, len(a)):
            if a[i] == 'C' and a[i-1] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                flag = False

    if flag:
        s1 = ''
        s2 = []
        nb = 0
        for i in range(len(a)):
            if a[i] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                s2.append(a[i])
            else:
                s1 = ''.join(a[i:])
                break

        s2 = s2[::-1]
        for i in range(len(s2)):
            nb += a1[s2[i]] * 26**i

        print(f'R{s1}C{nb}')

    else:
        s1 = ''
        s2 = ''
        nb = ''
        for i in range(1, len(a)):
            if a[i] != 'C':
                s2 += a[i]
            else:
                nb = ''.join(a[i+1:])
                break

        nb = int(nb)
        i = 0
        while (nb % 26**i)+1 != nb:

            s1 += a2[(nb % 26**i)+1]
            i += 1
            nb -= (nb % 26**i)+1

        print(s1)

        print(s1+s2)
