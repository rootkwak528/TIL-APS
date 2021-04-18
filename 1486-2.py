def f(i, s):
    global ans

    if ans == B:
        return
    if s > ans:
        return
    if i == N:
        if s >= B:
            ans = min(ans, s)
        return
    if s + rs[i] < B:
        return

    f(i + 1, s + H[i])
    f(i + 1, s)

T = int(input())
for test_case in range(1, T + 1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))

    rs = H[:]
    for i in range(N - 2, -1, -1):
        rs[i] += rs[i + 1]

    ans = sum(H)
    f(0, 0)
    print('#{} {}'.format(test_case, ans - B))