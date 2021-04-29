  N = 3
  arr = [1, 2, 3]  # 우리가 활용할 데이터
  sel = [0] * N   # a리스트(내가 해당 원소를 뽑았는지 체크)
  def powerset(idx):
      if idx == N:
          print(*sel)
          return
      sel[idx] = 0   # idx 자리의 원소를 뽑고 간다.
      powerset(idx+1)
      sel[idx] = 1   # idx 자리를 안뽑고 간다.
      powerset(idx+1)
  powerset(0)
  # output
  # 0 0 0
# 0 0 1
  # 0 1 0
# 0 1 1
  # 1 0 0
# 1 0 1
  # 1 1 0
  # 1 1 1


