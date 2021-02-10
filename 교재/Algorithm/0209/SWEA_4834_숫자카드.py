
T = int(input())

for i in range(T):
    N = int(input())
    A = list(map(int, input()))
    c = [0 for _ in range(10)]

    max_c = 0
    index_c = 0
    for a in A:
        c[a] += 1

        if c[a] > max_c:
            max_c = c[a]
            index_c = a

        # 개수가 같은 숫자일 때
        elif c[a] == max_c:
            if a > index_c:
                index_c = a
                max_c = c[a]

    print('#{} {} {}'.format(i+1, index_c, max_c))


