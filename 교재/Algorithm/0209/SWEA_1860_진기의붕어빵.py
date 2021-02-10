'''
N : 사람수
0초부터 붕어빵 만들고
M초 시간에 K개 붕어빵 나와

'''

T = int(input())
for i in range(T):
    N, M, K = map(int, input().split())
    num = list(map(int, input().split()))

    for j in range(len(num) - 1, 0, -1):
        for k in range(j):
            if num[k] > num[k + 1]:
                num[k], num[k + 1] = num[k + 1], num[k]

    impossible = 0
    for s in range(len(num)):

        if num[s] < M:
            impossible += 1
            break

        elif (num[s] // M * K) - s >= 1:
            continue

        elif (num[s] // M * K) - s < 1:
            impossible += 1
            break

    if impossible > 0:
        print('#{} {}'.format(i + 1, 'Impossible'))
    else:

        print('#{} {}'.format(i + 1, 'Possible'))






