T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    answer = []
    for n in [50000, 10000, 5000, 1000, 500, 100, 50, 10]:
        answer.append(str(N//n))
        N %= n

    print('#%d' % (test_case), ' '.join(answer), sep='\n')