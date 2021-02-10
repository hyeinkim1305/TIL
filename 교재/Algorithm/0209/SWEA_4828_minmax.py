
# 버블정렬로 풀게 되면 필요없는 연산 과정까지 하게 된다.
# 시간 복잡도가 N제곱
# 하지만 이 문제는 리스트 수가 길지 않아서 버블로 교수님이 푸신듯!

T = int(input())
for i in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    # 버블정렬
    for j in range(len(A)-1, 0, -1):
        for k in range(j):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]

    # 최대값과 최소값 차이
    output = A[-1] - A[0]

    print('#{} {}'.format(i+1, output))
