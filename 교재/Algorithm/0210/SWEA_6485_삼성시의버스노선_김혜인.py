
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    line = []
    stop = []
    output = []
    C = [0 for _ in range(5001)]

    for i in range(N):
        li = list(map(int, input().split()))
        line.append(li)

    P = int(input())

    for _ in range(P):
        p = int(input())
        stop.append(p)

    for k in line:
        for i in range(k[0], k[1]+1):
            if i in stop:
                C[i] += 1

    for s in stop:
        output.append(str(C[s]))

    print("#{} {}".format(tc, ' '.join(output)))

