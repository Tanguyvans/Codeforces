for _ in range(int(input())):
    word = input()

    nb = 0
    letters = []
    days = 1
    for i in word:
        if i not in letters:
            if nb < 3:
                letters.append(i)
                nb += 1
            else:
                days += 1
                letters = []
                letters.append(i)
                nb = 1

    print(days)
