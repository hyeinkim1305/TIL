
T = int(input())

for tc in range(1, T+1):
    # N : 카드의 개수
    N = int(input())
    card = input()
    # count 배열 생성
    count = [0] * 10

    max_count = -1
    max_num = -1

    # 카드 숫자 세기
    for i in card:
        count[int(i)] += 1

    for i in range(len(count)):
        if max_count <= count[i]:   # 등호가 들어간 이유는 숫자가 크면 바꿔야하니까
            max_num = i
            max_count = count[i]

    # 만약 뒤에서부터 시작한다면 = 이거는 필요 없다

    print("#{} {}".format(tc, max_num, max_count))

#######################################################################################
T = int(input())

for tc in range(1, T + 1):
    # N : 카드의 개수
    N = int(input())
    card = input()
    # count 배열 생성
    count = [0] * 10

    max_count = -1
    max_num = -1

    # 카드 숫자 세기
    for i in card:
        count[int(i)] += 1

        if max_count < count[int(i)]:
            max_count = count[int(i)]

    for i in range(len(count)-1, -1, -1):
        if max_count == count[i]:
            max_num = i
            break

    print("#{} {}".format(tc, max_num, max_count))
