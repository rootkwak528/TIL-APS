# 출처 : SWEA (https://swexpertacademy.com/)
# 문제번호 : 1249. 보급로
# 난이도 : D4

# bfs로 풀 수도 있고,
# dijkstra로도 풀 수 있지만,
# 여기서는 bfs로 풀겠음

def bfs(i, j):
    D[i][j] = 0
    queue = [(i, j)]
    rp = 0

    while rp < len(queue):
        i, j = queue[rp]
        rp += 1

        for di, dj in DELTA:
            ii, jj = i + di, j + dj
            if not (0 <= ii < N and 0 <= jj < N):
                continue

            new_d = D[i][j] + grid[ii][jj]
            if D[ii][jj] > new_d:
                D[ii][jj] = new_d
                queue.append((ii, jj))

DELTA = [[-1, 0], [1, 0], [0, -1], [0, 1]]
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input())) for _ in range(N)]
    D = [[float('inf')] * N for _ in range(N)]

    bfs(0, 0)
    print('#%d %d' % (test_case, D[-1][-1]))
