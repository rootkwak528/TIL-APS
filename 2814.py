# 출처 : SWEA (https://swexpertacademy.com/)
# 문제번호 : 2814 최장 경로
# 난이도 : D3

def longest(s):
    global L

    if not edges[s]:
        L = max(L, sum(V))
        return

    for e in edges[s]:
        if not V[e]:
            V[e] = 1
            longest(e)
            V[e] = 0
    else:
        L = max(L, sum(V))
        return

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    edges = [[] for _ in range(N + 1)]
    for _ in range(M):
        s, e = map(int, input().split())
        edges[s].append(e)
        edges[e].append(s)

    V, L = [0] * (N + 1), 0
    for s in range(1, N + 1):
        V[s] = 1
        longest(s)
        V[s] = 0

    print('#%d %d' % (test_case, L))