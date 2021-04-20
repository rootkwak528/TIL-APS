# 출처 : SWEA (https://swexpertacademy.com/)
# 문제번호 : 2806
# 난이도 : D3
# 실행시간 : N10 = 0.05s, N11 = 0.24s, N12 = 1.27s,
#         N13 = 7.11s, N14 = 43.06s
#         >> 2806-1 보다 약 4~5배 빠름!

def n_queen(i):
    if i == N:
        return 1
    rtn = 0
    for j in range(N):
        # 아이디어 : 직사각형 그리드에서 대각선은 i+j이나 i-j가 동일한 칸들로 표현될 수 있다!
        if not b[j] and not l[i+j] and not r[i-j]:
            b[j] = l[i+j] = r[i-j] = 1
            rtn += n_queen(i + 1)
            b[j] = l[i+j] = r[i-j] = 0
    return rtn

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    grid = [[0] * N for _ in range(N)]

    b, l, r = [0] * N, [0] * 2 * N, [0] * 2 * N
    print('#%d %d' % (test_case, n_queen(0)))