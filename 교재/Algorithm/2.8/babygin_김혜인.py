# 탐욕, 순열
# baby gin : 숫자 카드 6개를 임의로 뽑았을 때, 런과 트리플릿으로 구성되어 있는 경우
# 444345 입력받으면 count 배열 만들고 각각 count하고
# 리스트 012345678 처움에는 0 0 0 0 0
# run 조사 숫자가 연달아 3개 가 있으면 run, 한번씩 체크 끝났으면
# 하나씩 지워
# run 끝나면 triplet에서 3개있느거 triplet하고, 3을 지운다

num = 1564111
c = [0] * 12


Run = False
Triplet = False

for n in str(num):
    c[int(n)] += 1

for i in range(len(c)):
    if (c[i] != 0) and (c[i+1] != 0) and (c[i+2] != 0):
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        Run = True

for j in range(len(c)):
    if c[j] >= 3:
        c[j] -= 3
        Triplet = True

print(Run)
print(Triplet)
print(c)
