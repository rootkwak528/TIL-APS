# 출처 : SWEA (https://swexpertacademy.com/)
# 문제번호 : 2806
# 난이도 : D3
# 실행시간 : N10 = 0.21s, N11 = 1.02s, N12 = 5.48s,
#         N13 = 31.11s, N14 = 3:13.96s

def n_queen(i):
    if i == N:
        return 1
    rtn = 0
    for j in range(N):
        if not grid[i][j]:
            # 백트래킹
            for di, dj in DELTA:
                new_i, new_j = i + di, j + dj
                while 0 <= new_i < N and 0 <= new_j < N:
                    grid[new_i][new_j] += i + 1
                    new_i += di
                    new_j += dj

            rtn += n_queen(i + 1)

            # 원복
            for di, dj in DELTA:
                new_i, new_j = i + di, j + dj
                while 0 <= new_i < N and 0 <= new_j < N:
                    grid[new_i][new_j] -= i + 1
                    new_i += di
                    new_j += dj

    return rtn

DELTA = [[1, 0], [1, 1], [1, -1]]
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    grid = [[0] * N for _ in range(N)]

    print('#%d %d' % (test_case, n_queen(0)))