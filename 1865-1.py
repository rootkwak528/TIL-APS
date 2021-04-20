# 출처 : SWEA (https://swexpertacademy.com/)
# 문제번호 : 1865
# 난이도 : D4
# 실행결과 : 메모리 67,368 kb, 실행시간 5,021 ms

def book(i, x):
    global answer
    if i == N:
        answer = max(answer, x)
        return
    # 백트래킹 요소 : 현재까지 능률이 답 이하면 skip
    if x <= answer:
        return
    for j in range(N):
        if not booked[j]:
            booked[j] = 1
            book(i + 1, x * workers[i][j])
            booked[j] = 0

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    workers = [list(map(lambda x: int(x)/100, input().split())) for _ in range(N)]

    answer = 0
    booked = [0] * N
    book(0, 1)
    print('#%d %f' % (test_case, round(answer*100, 6)))