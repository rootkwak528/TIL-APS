def recursive(i, j, s):
    if (not 0 <= i < 4) or (not 0 <= j < 4):
        return
    if len(s) == 7:
        answer.add(int(s))
    else:
        s += grid[i][j]
        for di, dj in DELTA:
            recursive(i + di, j + dj, s)

DELTA = [[1, 0], [-1, 0], [0, 1], [0, -1]]
T = int(input())
for test_case in range(1, T + 1):
    grid = [input().split() for _ in range(4)]

    answer = set()
    for i in range(4):
        for j in range(4):
            recursive(i, j, '')

    print('#%d %d' % (test_case, len(answer)))