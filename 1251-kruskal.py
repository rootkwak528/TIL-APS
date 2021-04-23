# 출처 : SWEA (https://swexpertacademy.com/)
# 문제번호 : 1251. 하나로
# 난이도 : D4

# kruskal

def find_set(x):
    while x != p[x]:
        x = p[x]
    return x

def union(x, y):
    p[find_set(y)] = find_set(x)

def kruskal():
    MST = []
    roads.sort()

    idx = 0
    while len(MST) < N - 1:
        w, x, y = roads[idx]
        idx += 1

        if find_set(x) != find_set(y):
            union(x, y)
            MST.append((x, y, w))

    return MST

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    p = list(range(N))
    roads = []
    for i in range(N - 1):
        for j in range(i + 1, N):
            roads.append(((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2, i, j))

    answer = sum(x[2] for x in kruskal()) * E
    print('#%d %d' % (test_case, round(answer)))
