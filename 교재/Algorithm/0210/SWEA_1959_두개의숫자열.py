
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N >= M:
        long = N
        short = M
        long_li = A
        short_li = B
    else:
        long = M
        short = N
        long_li = B
        short_li = A

    max_output = 0
    for i in range(short):
        max_output += long_li[i] * short_li[i]


    for t in range(1, long-short+1):
        output = 0
        for j in range(short):
            output += short_li[j] * long_li[t+j]
        if output > max_output:
            max_output = output

    print("#{} {}".format(tc, max_output))