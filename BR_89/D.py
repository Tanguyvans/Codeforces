def reccursion(t1, t2, m_t1, m_t2):
    if t1 == 0 and t2 == 0:
        return 1

    elif (t1, t2, m_t1, m_t2) in dp:
        return dp[(t1, t2, m_t1, m_t2)]

    else:
        s1 = 0
        s2 = 0

        if t1 and m_t1:
            s1 = reccursion(t1-1, t2, m_t1-1, k2)

        if t2 and m_t2:
            s2 = reccursion(t1, t2-1, k1, m_t2-1)

        sol = (s1 + s2) % 10**8
        dp[(t1, t2, m_t1, m_t2)] = sol

        return sol


n1, n2, k1, k2 = map(int, input().split())
dp = dict()
sol = reccursion(n1, n2, k1, k2)

print(sol)
