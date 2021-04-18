T = int(input())
for test_case in range(1, T + 1):
    N, B, H = *map(int, input().split()), list(map(int, input().split()))
    towers = [0]
    for i in range(N):
        towers += list(map(lambda x: x + H[i], towers))

    for tower in sorted(towers):
        if tower >= B:
            print('#%d %d' % (test_case, tower - B))
            break

"""
1
5 16
1 3 3 5 6
"""