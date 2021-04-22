# dijkstra

def dijkstra(node):
    D = [float('inf')] * (N + 1)
    V = [0] * (N + 1)

    D[node] = 0
    for _ in range(N + 1):
        node = min((w, s) for s, w in enumerate(D) if not V[s])[1]
        V[node] = 1

        for e, w in roads[node]:
            if not V[e]:
                D[e] = min(D[e], w + D[node])

    return D

T = int(input())
for test_case in range(1, T + 1):
    N, E = map(int, input().split())

    roads = [[] for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        roads[s].append((e, w))

    print('#%d %d' % (test_case, dijkstra(0)[N]))

"""
3
2 3
0 1 1
0 2 6
1 2 1
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10
"""