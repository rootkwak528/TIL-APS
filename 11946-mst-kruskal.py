# kruskal

def find_set(x):
    while x != p[x]:
        x = p[x]
    return x

def union(x, y):
    p[find_set(y)] = find_set(x)

def kruskal(node):
    MST = []
    roads.sort(key=lambda x: x[2])
    for x, y, w in roads:
        if find_set(x) != find_set(y):
            union(x, y)
            MST.append((x, y, w))
    return MST

T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    roads = [tuple(map(int, input().split())) for _ in range(E)]

    p = list(range(V + 1))
    print('#%d %d' % (test_case, sum(w for _, _, w in kruskal(0))))
