def dijkstra(i, w):
    for _e, _w in edges[i]:
        if D[_e] > w + _w:
            D[_e] = w + _w
            dijkstra(_e, w + _w)

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    D = [float('inf')] * N
    edges = [[] for _ in range(N)]
    for _ in range(M):
        s, e, w = input().split()
        s, e, w = ord(s) - 97, ord(e) - 97, int(w)
        edges[s].append((e, w))

    D[0] = 0
    dijkstra(0, 0)
    print('#%d %s' % (test_case, ' '.join(map(str, D))))