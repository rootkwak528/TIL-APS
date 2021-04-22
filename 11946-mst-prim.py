# prim & heap

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

def heapify(arr):
    heap = []
    for ent in arr:
        heappush(heap, ent)
        print(heap)
    return heap

def prim(node):
    MST = []
    heap = []
    visited = {node}
    queue, rp = [node], 0

    while len(MST) < V:
        cur = queue[rp]
        rp += 1

        for road in roads[cur]:
            heappush(heap, road)

        while heap:
            w, s, e = heappop(heap)
            if e in visited:
                continue

            queue += [e]
            visited.add(e)
            MST.append((s, e, w))
            break

    return MST

T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())

    roads = [[] for _ in range(V + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        roads[s].append((w, s, e))
        roads[e].append((w, e, s))

    print('#%d %d' % (test_case, sum(w for _, _, w in prim(0))))
