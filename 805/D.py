alphabet = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16,
            'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

alpha = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p',
         17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}

for _ in range(int(input())):
    n = input()
    n = [i for i in n]

    a = [[] for i in range(len(n))]
    total = 0
    for i in range(len(n)):
        a[i] = [i, True, alphabet[n[i]]]
        total += alphabet[n[i]]

    nb = int(input())
    a = sorted(a, key=lambda x: -x[2])
    i = 0
    while nb < total:
        total -= a[i][2]
        a[i][1] = False
        i += 1

    a = sorted(a, key=lambda x: x[0])

    for i in range(len(n)):
        if a[i][1]:
            print(alpha[a[i][2]], end='')

    print()
