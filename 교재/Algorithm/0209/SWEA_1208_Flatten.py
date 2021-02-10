for tc in range(1, 11):
    N = int(input())
    li = list(map(int, input().split()))

    while N >= 0:
        # 초기값 설정
        max_li = 0
        min_li = 101
        max_idx = 0
        min_idx = 0

        # 최대값, 최소값 찾기
        for i, n in enumerate(li):
            if n > max_li:
                max_li = n
                max_idx = i
            if n < min_li:
                min_li = n
                min_idx = i
        # 평준화된 것이 0일때
        if max_li == min_li:
            output = 0
            break
        # 블럭옮기기
        li[max_idx] -= 1
        li[min_idx] += 1

        N -= 1
    # 최대 최소값 찾기
    for j in li:
        if j > max_li:
            max_li = j
        if j < min_li:
            min_li = j
    output = max_li - min_li
    print('#{} {}'.format(tc, output))
