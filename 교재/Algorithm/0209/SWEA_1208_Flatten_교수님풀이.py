# 결국 필요한건 최고값이 있는 인덱스, 최저값이 있는 인덱스

# 최저 높이의 상자 인덱스 위치 반환
def min_search():
    min_value = 987654321
    min_idx = -1
    # 최저 높이 찾기
    for i in range(len(box)):
        if box[i] < min_value:
            min_value = box[i]
            min_idx = i

    return min_idx

def max_search():
    max_value = 0
    max_idx = -1

    for i in range(len(box)):
        if box[i] > max_value:
            max_value = box[i]
            max_idx = i
    return max_idx

for tc in range(1, 10+1):
    # N : 덤프 횟수
    N = int(input())

    box = list(map(int, input().split()))

    # N번 덤프
    for i in range(N):
        # 최고높이 상자 한칸 내리기
        box[max_search()] -= 1
        # 최저 높이 상자 한칸 올리기
        box[min_search()] += 1

    print("#{} {}".format(tc, box[max_search()]-box[min_search()]))

#####################################################################
# sol2

# 버블 정렬을 해서 시작
def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

for tc in range(1, 11):
    N = int(input())
    box = list(map(int, input().split()))

    for i in range(N):
        bubble_sort(box)   # 값이 매우 커진다면 매우 버블정렬하는 것은 비효율적
        box[0] += 1
        box[-1] -= 1
    bubble_sort(box)

    print('#{} {}'.format(tc, box[-1] - box[0]))

#######################################################################
# sol3
for tc in range(1, 10+1):
    # N : 덤프 횟수
    N = int(input())
    box = list(map(int, input().split()))

    # 높이 카운트
    h_cnt = [0] * 101
    # 값 초기화
    min_value = 100
    max_value = 1

    # 박스의 높이를 카운트 하면서 최고점과 최저점을 찾기
    for i in range(100):
        h_cnt[box[i]] += 1
        if box[i] > max_value:
            max_value = box[i]
        if box[i] < min_value:
            min_value = box[i]

    while N > 0 and min_value < max_value-1:   # 이 부분 잘 생각하기
        h_cnt[min_value] -= 1
        h_cnt[min_value+1] += 1

        h_cnt[max_value] -= 1
        h_cnt[max_value-1] += 1

        if box[min_value] == 0:
            min_value += 1
        if box[max_value] == 0:
            max_value -= 1

        N -= 1

    print("#{} {}".format(tc, max_value-min_value))
