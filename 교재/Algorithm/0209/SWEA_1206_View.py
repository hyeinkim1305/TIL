# 입력을 파일로 읽어오기
import sys
sys.stdin = open("input.txt",'r')


for i in range(1, 11):
    N = int(input())
    c = [[0 for _ in range(255)] for _ in range(N)]
    li = list(map(int, input().split()))

    for t in range(N):
        for k in range(li[t]):
            c[t][k] = 1

    output = 0
    for j in range(2, N-1):
        if li[j] > li[j-1] and li[j] > li[j-2] and li[j] > li[j+1] and li[j] > li[j+2]:
            for s in range(li[j]-1, -1, -1):
                if c[j-1][s] == 0 and c[j-2][s] == 0 and c[j+1][s] == 0 and c[j+2][s] == 0:
                    output += 1

    print('#{} {}'.format(i, output))


