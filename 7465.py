# 출처 : SWEA (https://swexpertacademy.com/)
# 문제번호 : 7465. 창용 마을 무리의 개수
# 난이도 : D4

# disjoint set 문제

def find_set(x):
    while x != p[x]:
        x = p[x]
    return x

def union(x, y):
    p[find_set(y)] = find_set(x)

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    p = list(range(N + 1))
    for _ in range(M):
        x, y = map(int, input().split())
        union(x, y)

    print('#%d %d' % (test_case, sum(x == p[x] for x in range(N + 1)) - 1))
