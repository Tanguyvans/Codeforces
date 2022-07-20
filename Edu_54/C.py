from tkinter import N


for _ in range(int(input())):
    n = int(input())

    if n == 0:
        print('Y', 0, 0)
    elif 0 < n < 4:
        print('N')
    else:
        d = n**2 - n*4
        a = (n+d**(1/2))/2
        print('Y', a, n-a)
