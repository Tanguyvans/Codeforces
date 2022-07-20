for _ in range(int(input())):

    n = int(input())

    answer = [i+1 for i in range(n)]
    for i in range(n):
        for j in range(n):
            print(j)

            print([(a+j) % 5 for a in answer])
