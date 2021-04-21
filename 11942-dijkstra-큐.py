def dijkstra(i):
    queue, D, V = [0] * N, [float('inf')] * N, [0] * N
    wp = rp = 0

    D[i] = 0
    queue[wp] = (0, i)
    wp += 1

    while wp > rp:
        weight, cur = queue[rp]
        rp += 1
        V[cur] = 1

        for e, w in edges[cur]:
            if not V[e]:
                if D[e] > weight + w:
                    D[e] = weight + w

        tmp = []
        for s, w in enumerate(D):
            if not V[s]:
                tmp.append((w, s))

        if tmp:
            queue[wp] = min(tmp)
            wp += 1

    return ' '.join(map(str, D))

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    edges = [[] for _ in range(N)]
    for _ in range(M):
        s, e, w = input().split()
        s, e, w = ord(s) - 97, ord(e) - 97, int(w)
        edges[s].append((e, w))

    print('#%d %s' % (test_case, dijkstra(0)))

"""
3
6 11
a b 3
a c 5
b c 2
b d 6
c b 1
c d 4
c e 6
d e 2
d f 3
e a 3
e f 6
6 10
a b 3
a c 4
b d 5
c b 1
c d 4
c e 5
d f 4
d e 3
e a 3
e f 5
6 10
a b 4
a c 2
a f 25
b d 8
b e 7
c b 1
c e 4
d f 6
e d 5
e f 12
"""