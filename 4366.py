# 출처 : SWEA (https://swexpertacademy.com/)
# 문제번호 : 4366
# 난이도 : D4

T = int(input())
for test_case in range(1, T + 1):
    b, t = input(), input()
    b_num, t_num = int(b, 2), int(t, 3)

    b_set = set()
    for i in range(len(b) - 1):
        b_set.add(b_num ^ 1 << i if b[-i-1] == '1' else b_num | 1 << i)

    t_set = set()
    for i in range(len(t)):
        digits = [0, 1, 2] if i < len(t) - 1 else [1, 2]
        for digit in digits:
            if digit != int(t[-i-1]):
                t_set.add(t_num - (int(t[-i-1]) - digit) * 3**i)

    print('#%d %d' % (test_case, (b_set & t_set).pop()))

"""
4
1010
212
1110
121
1001100111001
20202021
10001010100011011000000101000
202020202021212121
"""