T = int(input())

for tc in range(1, T+1):
    # N : 원소의 개수
    # M : 구간의 길이
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    max_value = 0
    min_value = 987654321

    for i in range(N-M+1):
        tmp = 0

        for j in range(M):
            tmp += nums[i+j]
        # 여기까지 하면 한 구간의 합이 나옴

        # for j in nums[i:i+M]:
        #     tmp += j
        # tmp = sum(nums[i:i+M])

        # 이렇게 하면 정렬 안써도됨됨
       if max_value < tmp:
            max_value = tmp
        if min_value > tmp:
            min_value = tmp

    print("#{} {}".format(tc, max_value - min_value))

#############################################################################
# sol2
# 첫구간만 구하고 가장 앞에꺼 버리고 다음에 수 추가하면 다음 구간꺼 합이 나옴
# 증복된 연산 피하기

T = int(input())

for tc in range(1, T+1):
    # N : 원소의 개수
    # M : 구간의 길이
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    max_value = 0
    min_value = 987654321

    # 첫 구간은 구해 놓자..
    tmp = 0
    for i in range(M):
        tmp += nums[i]

    max_value = tmp
    min_value = tmp

    #0부터 4까지 더했다면 5부터 7까지만 더 연산하면 되니까 M,N 인 것
    for i in range(M, N):
        # 새로운 구간의 합을 아주 아주 간단하게 구할 수 있음
        tmp = tmp + nums[i] - nums[i - M] # 새롭게 추가될 거 더하고 젤 앞에꺼 뺌

        if max_value < tmp:
            max_value = tmp
        if min_value > tmp:
            min_value = tmp

    print("#{} {}".format(tc, max_value - min_value))




