alphabet = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7,
            'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}


for _ in range(int(input())):

    n, m = map(int, input().split(' '))

    words = []

    for i in range(n):
        words.append(input())

    r = []
    for i in range(len(words)):
        for j in range(len(words)):
            if i == j:
                continue

            ans = 0
            for k in range(m):
                ans += abs(alphabet[words[i][k]] - alphabet[words[j][k]])

            r.append(ans)

    print(min(r))
