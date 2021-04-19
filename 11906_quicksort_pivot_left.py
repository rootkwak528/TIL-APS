# 출처 : SWEA (https://swexpertacademy.com/)
# 문제번호 : 11906
# 난이도 : D3

def quicksort(s, e):
    if s >= e:
        return

    # pivot left
    pivot = s
    i = j = s + 1

    while j <= e:
        if arr[j] < arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1

    # 기준이 i-1 인덱스
    arr[pivot], arr[i-1] = arr[i-1], arr[pivot]
    quicksort(s, i - 2)
    quicksort(i, e)

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    quicksort(0, N - 1)
    print('#%d %d' % (test_case, arr[N//2]))