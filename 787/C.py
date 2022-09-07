for _ in range(int(input())):
    a = input()
    a = [i for i in a]

    one = 0
    zero = -1
    ans = 0
    for i in range(len(a)):

        if a[i] == '1':
            one = i

        if zero == -1 and a[i] == '0':
            zero = i

    print(len(a[one:zero])+1)
