
T = int(input())
number = [2, 3, 5, 7, 11]

for tc in range(1, T+1):
    N = int(input())
    count = []

    for num in number:
        cnt = 0
        while N % num == 0:
            N = N // num
            cnt += 1

        count.append(str(cnt))

    print('#{} {}'.format(tc, " ".join(count)))

