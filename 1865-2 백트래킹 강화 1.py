# 출처 : SWEA (https://swexpertacademy.com/)
# 문제번호 : 1865
# 난이도 : D4
# 실행결과 : 메모리 63,412 kb, 실행시간 1,411 ms
#         >> 1865-1 보다 약 3~4배 빠름!

def book(j, rate):
    global answer
    if j == N:
        answer = max(answer, rate)
        return
    # 백트래킹 강화 : 현재 능률에 최대값기준 곱한 값이 답보다 작으면 skip
    if rate * top_rate[j] <= answer:
        return
    for i in range(N):
        if not booked[i]:
            booked[i] = 1
            book(j + 1, rate * workers[i][j])
            booked[i] = 0

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    workers = [list(map(lambda x: int(x)/100, input().split())) for _ in range(N)]

    # 백트래킹 강화 : "작업(열)"에 대한 최대값 기준 정하기
    top_rate = [max(col) for col in zip(*workers)]
    for i in range(N - 2, -1, -1):
        top_rate[i] *= top_rate[i + 1]

    answer = 0
    booked = [0] * N
    book(0, 1)
    print('#%d %f' % (test_case, round(answer*100, 6)))

"""
1
8
15 16 93 35 43 17 18 94
50 27 69 69 46 71 65 60
88 8 28 70 52 87 40 47
38 32 75 49 73 23 95 94
94 93 18 5 72 72 4 50
77 62 43 32 76 57 12 12
28 87 91 46 23 59 7 88
60 97 79 21 28 40 71 21
"""