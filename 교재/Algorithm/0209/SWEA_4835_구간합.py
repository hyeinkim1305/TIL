
T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    output = []

    for j in range(N-M+1):
        out = 0
        for s in range(j, j+M):
            out += A[s]
        output += [out]

    # 이렇게 굳이 안해도 될 듯?
    for k in range(len(output)-1, 0, -1):
        for t in range(k):
            if output[t] > output[t+1]:
                output[t], output[t+1] = output[t+1], output[t]

    answer = output[-1] - output[0]

    print('#{} {}'.format(i+1, answer))
