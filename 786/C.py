for _ in range(int(input())):

    a = input()
    a = [i for i in a]
    la = len(a)

    word = input()
    if word == 'a':
        print(1)
        continue

    word = [i for i in word]

    if 'a' in word:
        print(-1)
    else:

        ans = 2**la

        print(ans)
