# 출처 : SWEA (https://swexpertacademy.com/)
# 문제번호 : 11905
# 난이도 : D3

def mergesort(arr):
    if len(arr) == 1:
        return arr

    # 분할
    mid = len(arr) // 2
    arr1 = mergesort(arr[:mid])
    arr2 = mergesort(arr[mid:])

    # 병합조건과는 상관 없는 문제의 조건
    # 분할된 왼쪽 배열의 마지막 수가 오른쪽 배열의 마지막 수보다 큰 경우의 수(cnt)를 출력하라
    global cnt
    cnt += arr1[-1] > arr2[-1]

    # 병합
    sorted_arr, j = [], 0
    for i in range(len(arr1)):
        while j < len(arr2) and arr2[j] < arr1[i]:
            sorted_arr.append(arr2[j])
            j += 1
        sorted_arr.append(arr1[i])

    sorted_arr.extend(arr2[j:])
    return sorted_arr

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = 0
    sorted_arr = mergesort(arr)
    print('#%d %d %d' % (test_case, sorted_arr[N//2], cnt))

"""
2
5
2 2 1 1 3
10
7 5 4 1 2 10 3 6 9 8
"""