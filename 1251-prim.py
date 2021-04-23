# 출처 : SWEA (https://swexpertacademy.com/)
# 문제번호 : 1251. 하나로
# 난이도 : D4

# prim

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

def prim(node):
    MST = []
    V = [0] * N
    heap = [(0, node, node)]

    while len(MST) < N:
        w, prev, node = heappop(heap)

        if V[node]:
            continue
        V[node] = 1
        MST.append((prev, node, w))

        for w, i, j in roads[node]:
            if not V[j]:
                heappush(heap, (w, i, j))

    return MST

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    roads = [[] for _ in range(N)]
    for i in range(N - 1):
        for j in range(i + 1, N):
            L2 = (X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2
            roads[i].append((L2, i, j))
            roads[j].append((L2, j, i))

    answer = sum(x[2] for x in prim(0)) * E
    print('#%d %d' % (test_case, round(answer)))
