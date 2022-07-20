from collections import defaultdict
import sys
import threading
sys.setrecursionlimit(10**6)
threading.stack_size(10**8)
s = []


def dfs(graph, n, p, level):
    penalty = 1
    for c in graph[n]:
        if c == p:
            continue
        penalty += dfs(graph, c, n, level + 1)
    s.append(level - penalty)
    return penalty


def main():
    n, k = map(int, input().split())
    g = [[] for i in range(n)]
    for i in range(n-1):
        u, v = map(int, input().split(' '))

        g[u-1].append(v-1)
        g[v-1].append(u-1)

    try:
        dfs(g, 0, None, 1)
    except Exception as e:
        print(e)

    m = sorted(s, reverse=True)
    print(sum(m[:k]))


t = threading.Thread(target=main)
t.start()
t.join()
