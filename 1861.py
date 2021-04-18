T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    N2 = N**2
    x, y = [0] * (N2 + 1), [0] * (N2 + 1)
    for i in range(N):
        for j in range(N):
            n = grid[i][j]
            x[n], y[n] = i, j

    ans = max_n = tmp = 1
    for n in range(1, N2):
        if tmp + N2 - n <= ans:
            break
        if (x[n] == x[n+1] and abs(y[n] - y[n+1]) == 1) or\
                (y[n] == y[n+1] and abs(x[n] - x[n+1]) == 1):
            tmp += 1
        else:
            if tmp > ans:
                ans = tmp
                max_n = n - tmp + 1
            tmp = 1

    if tmp > ans:
        ans = tmp
        max_n = N2 - tmp + 1

    print('#%d %d %d' % (test_case, max_n, ans))
