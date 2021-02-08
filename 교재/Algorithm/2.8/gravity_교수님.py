
'''
3
9
7 4 2 0 0 6 0 7 0
9
7 4 2 0 0 6 7 7 0
20
52 56 38 77 43 31 11 87 68 64 88 76 56 59 46 57 75 85 65 53
'''

# 사실은 가장 꼭대기층만 고려해도 되는 것
# 1말고 나머지는 0으로 채우면 되는구나 , 나는 0으로 안채워서 고민했음

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    boxTop = list(map(int, input().split()))
    # 옆으로 돌려놓은 모양, 100칸만큼 있는 것들을 N번 반복, 이중리스트
    #  (_는 의미없는 거 느낌)
    room = [[0 for _ in range(100)] for _ in range(N)]
    # 행을 순회하면서 N번 반복
    for i in range(N):
        for j in range(boxTop[i]):
            room[i][j] = 1

    Max = 0  # 최대 낙차 저장
    for i in range(N):   # 각 행마다
        if boxTop[i] > 0 :
            dist = 0
            # 내려오면서 0칸을 다 센다.
            for j in range(i+1, N):
                if room[j][boxTop[i]-1] == 0:
                    dist += 1
            if dist > Max:
                Max = dist

    print('#{} {}'.format(tc, Max))





