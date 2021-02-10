# 아침이 되어서야 풀 수 있었습니다..ㅜ

# while 종점 도착할 때까지
# 일단 최대한 이동해보고 만약 그 숫자가 없으면 탐색
# 있으면 그 숫자가 다시 시작 숫자가 되고

tc = int(input())

for t in range(1, tc+1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))

    s = 0
    count = 0
    while s+K < N:
        num = 0
        if s + K in charge:
            s = s+K
            count += 1
            num += 1
        else:
            for i in range(s+K-1, s, -1):
                if i in charge:
                    s = i
                    count += 1
                    num += 1
                    break
                else:
                    num = 0
            if num == 0:
                break

    if num > 0:
        print('#{} {}'.format(t, count))
    else:
        print('#{} {}'.format(t, num))



