a = input()

for i, ai in enumerate(a):
    if i == 0 and int(ai) == 9:
        print(9, end='')
    else:
        print(min(int(ai), 9-int(ai)), end='')
