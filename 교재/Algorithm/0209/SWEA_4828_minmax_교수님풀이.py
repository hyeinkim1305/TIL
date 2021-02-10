
def Bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# 전체 테스트 케이스 수
for tc in range(1, int(input())+1):
    N = int(input())
    number = list(map(int, input().split()))

    # # sol1 정렬 후 출력
    # Bubble_sort(number)
    # print("#{} {}".format(tc, number[-1]-number[0]))

    # sol2 최대값, 최소값만 찾기
    max_value = 0
    min_value = 987654321

    for i in range(N):
        # 최대값 갱신
        if max_value < number[i]:
            max_value = number[i]
        # 최소값 갱신
        if min_value > number[i]:
            min_value = number[i]

    print("#{} {}".format(tc, max_value-min_value))
