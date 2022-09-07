for _ in range(int(input())):
    n, k = map(int, input().split())

    a = input()
    a = [ord(i)-97 for i in a]
    seq = {i: chr(i+97) for i in range(26)}

    sol = ''
    for i in range(len(a)):
        ans = a[i]

        while seq[ans] != 'a' and k >0: 
            

        

        sol += chr(ans+97)

    print(sol)
