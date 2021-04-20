# 출처 : SWEA (https://swexpertacademy.com/)
# 문제번호 : 1865
# 난이도 : D4
# 실행결과 : 메모리 64,836 kb, 실행시간 1,564 ms
#         >> 1865-1 보다 약 3~4배 빠름!

def book(i, rate):
    global answer
    if i == N:
        answer = max(answer, rate)
        return
    # 백트래킹 강화 : 현재 능률에 최대값기준 곱한 값이 답보다 작으면 skip
    if rate * top_rate[i] <= answer:
        return
    for j in range(N):
        if not booked[j]:
            booked[j] = 1
            book(i + 1, rate * workers[i][j])
            booked[j] = 0

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    workers = [list(map(lambda x: int(x)/100, input().split())) for _ in range(N)]

    # 백트래킹 강화 : "작업자(행)"에 대한 최대값 기준 정하기
    top_rate = [max(worker) for worker in workers]
    for i in range(N - 2, -1, -1):
        top_rate[i] *= top_rate[i + 1]

    answer = 0
    booked = [0] * N
    book(0, 1)
    print('#%d %f' % (test_case, round(answer*100, 6)))