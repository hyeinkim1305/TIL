# 입력을 파일로 읽어오기
import sys
sys.stdin = open("input.txt",'r')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    dist = 0

    for i in range(2, N-2):  # 양쪽 두 칸 빼기
        check = 0   # 조망권이 가능한 범위
        Max = 0     # 주변 빌딩 중 높은 빌딩
        for j in range(1, 3):

            # 기준 빌딩보다 주변 빌딩이 높으면 스킵
            if arr[i] < arr[i-j] or arr[i] < arr[i+j]:
                break

            if Max < arr[i-j]:
                Max = arr[i-j]
            if Max < arr[i+j]:
                Max = arr[i+j]
            check += 1

        if check == 2:
            dist += arr[i] - max
    print('#{} {}'.format(tc, dist))

#################################################################
# sol2

# 입력을 파일로 읽어오기
import sys
sys.stdin = open("input.txt",'r')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    dist = 0

    for i in range(2, N-2):  # 양쪽 두 칸 빼기
        # 변수명 = 참 if 조건 else 거짓
        # 왼쪽 중 큰빌딩
        left = arr[i-2] if arr[i-1] < arr[i-2] else arr[i-1]
        # 오른쪽 중 큰 빌딩
        right = arr[i + 2] if arr[i + 1] < arr[i + 2] else arr[i + 1]
        top = left if left > right else right

        if arr[i] > top:
            dist += arr[i] - top

    print('#{} {}'.format(tc, dist))