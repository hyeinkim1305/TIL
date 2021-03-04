# dfs  &  bfs  정리

##### 코드 참고

0223 > 그래프경로_교수님풀이

0302 > 미로_교수님풀이 (2차원배열 _dfs, 스택)

0304 > 미로1 (2차원배열_dfs, bfs)

0304 > 노드의 거리(인접리스트 dict)



### 2차원 배열 dfs, bfs로 풀기 (+4방향탐색)

##### dfs 

1. ##### 재귀

```python
def dfs(r, c):
    arr[r][c] = 1	# 현재 정점 방문 표시하고

    for i in range(4):	# 4방향 탐색
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr > N-1 or nc < 0 or nc > N-1:
            continue
        if arr[nr][nc] == 3:	# 3이면 리턴 1
            return 1
        elif arr[nr][nc] == 0:	# 통로이면 재귀로 다시
            if dfs(nr, nc) == 1:     # 이 부분 중요 !! 그냥 리턴하면 안됨
                return 1
    return 0
```

2. ##### 스택

```python
def dfs():
    # 상하좌우를 찾기 위한 델타
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    #스택
    s = []
    s.append([sr, sc])  	# 시작점
    # 방문배열은 굳이 만들지 않고 왔던 길을 막아버리는 방식!
    arr[sr][sc] = 1  	# 지나온 곳은 1로
    while len(s) != 0:
        n = s.pop()     	# 스택에서 좌표 하나 꺼내옴
        for k in range(4):
            nr = n[0] + dr[k]
            nc = n[1] + dc[k]
            if nr >= 0 and nr < N and nc >= 0 and nc < N:  	# 탐색가능한지 체크
                if arr[nr][nc] == 3:  	# 도착점을 찾으면
                    return 1  	# 1을 가지고 리턴
                elif arr[nr][nc] == 0:  	# 갈 수 있는 길이면
                    s.append([nr, nc])  	# 스택에 넣음
                    arr[n[0]][n[1]] = 1     	# 방문했다고 표시
    return 0   		# 다 가봤는데 도착점 못 찾음
```

-- bfs 풀이방식과 유사한데 스택을 활용해서 뒤에서 정점들을 꺼낸다는 점이 다른듯!



##### bfs

1. ##### 큐 활용

```python
def bfs(r, c):
    q = []			# 큐 만들고 현재 정점 넣고 방문 표시
    q.append([r, c])
    arr[r][c] = 1

    while q:		# 큐가 존재할동안
        cur = q.pop(0)		# 정점 pop
        for i in range(4):
            nr = cur[0] + dr[i]
            nc = cur[1] + dc[i]
            if nr < 0 or nr > N-1 or nc < 0 or nc > N-1:
                continue
            if arr[nr][nc] == 3:
                return 1
            if arr[nr][nc] == 0:
                q.append([nr, nc])		# 인접정점을 q에 추가
                arr[nr][nc] = 1			# 방문 표시
    return 0
```

-- 2차원 배열이 아니면 visit따로 만들어서 방문 표시 해야함

-- 만약 거리구하기라면 따로 거리 배열을 만들거나 하고, pop한 노드의 거리에 + 1

