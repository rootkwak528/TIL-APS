# 출처 : SWEA (https://swexpertacademy.com/)
# 문제번호 : 1795. 인수의 생일 파티
# 난이도 : D6

# 1. import heapq 대신 직접 heap 구현하였음
# 2. directed graph에서 왕복 최단거리를 구해야하므로
#    일반 그래프 [roads]와 방향을 뒤집은 [rev_roads]에 대해
#    dijkstra를 각각 한번씩 실행하였음

def heappush(heap, x):
    heap.append(x)
    cur = len(heap) - 1

    # percolate up
    while cur:
        parent = (cur - 1) // 2
        if heap[parent] > heap[cur]:
            heap[parent], heap[cur] = heap[cur], heap[parent]
            cur = parent
        else:
            break

def heappop(heap):
    if len(heap) == 1:
        return heap.pop()

    top = heap[0]
    heap[0] = heap.pop()
    cur = 0

    # percolate down
    while cur * 2 + 1 < len(heap):
        c1 = cur * 2 + 1
        c2 = cur * 2 + 2
        child = c1 if c2 == len(heap) or heap[c1] < heap[c2] else c2

        if heap[child] < heap[cur]:
            heap[child], heap[cur] = heap[cur], heap[child]
            cur = child
        else:
            break

    return top

def dijkstra(x, roads):
    D = [float('inf')] * (N + 1)
    V = [0] * (N + 1)

    D[x], cnt = 0, 0
    heap = []
    heappush(heap, (D[x], x))

    while cnt < N:
        weight, cur = heappop(heap)
        if V[cur]:
            continue

        V[cur] = 1
        cnt += 1

        for _weight, next in roads[cur]:
            if not V[next]:
                if D[next] > D[cur] + _weight:
                    D[next] = D[cur] + _weight
                    heappush(heap, (D[next], next))

    return D

T = int(input())
for test_case in range(1, T + 1):
    N, M, X = map(int, input().split())

    roads = [[] for _ in range(N + 1)]
    rev_roads = [[] for _ in range(N + 1)]

    for _ in range(M):
        s, e, w = map(int, input().split())
        roads[s].append((w, e))
        rev_roads[e].append((w, s))

    D = dijkstra(X, roads)
    rev_D = dijkstra(X, rev_roads)

    print('#%d %d' % (test_case, max(D[i] + rev_D[i] for i in range(1, N + 1))))