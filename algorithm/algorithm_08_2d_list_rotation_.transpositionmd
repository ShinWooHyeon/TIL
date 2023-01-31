# 2차원 리스트 순회
- 행 우선 순회를 할 경우 2중 for문에서 두 번째 for문을 행의 인덱스로 한다
- 열 우선 순회를 할 경우 2중 for문에서 두 번째 for문을 열의 인덱스로 한다.
```python
# 행 우선 순회 (3*4 2차원 리스트)
for i in range (4):
    for j in range(3):
        print(matrix[j][i])
# 열 우선순회
for i in range(3):
    for j in range(4):
        print(matrix[i][j])
```
- 2차원 리스트의 총합 : 이중 for문을 통해 각 요소 순회하면서 더해준다 
```python
#2차원 리스트의 합 참고
td_sum=sum(map(sum,matrix)) 
```

# 2차원 리스트 전치
- 전치: 행렬의 행과 열을 서로 바꿔주는 것
    - m*n 행렬의 전치: `n*m` 행렬을 인덱스로 받아 만들어준다
```python
#원래 행렬 matrix=3*4
trans_matrix=[[0]*3 for _ in range (4)]
for i in range(4):
    for j in range(3):
        trans_matrix[i][j]=matrix[j][i]
```

# 2차원 리스트 회전
- 2차원 리스트를 오른쪽으로 회전
```python
x=[[1,2,3],
   [4,5,6]
   [7,8,9]]
# 위 리스트를 오른쪽으로 회전하면
x=[[7,4,1],
   [8,5,2],
   [9,6,3] ]
```
1,2,3을 기준으로 볼 경우 원래 열이 행이된다 <(0,0),(0,1),(0,2)가 (0,2),(1,2),(2,2>)로 변경
- 바뀐 행렬의 열은 원래 행렬의 행이 앞에 있는만큼 회전시 뒤로가게된다
- m*n 행렬의 에서 i행을 회전시킬 경우 바뀐 행렬의 열은 `n-m-1`(인덱스기 때문에 1 뺀다)
```python
rotated=[[0]*n for _ in range(n)]
for i in range (m):
    for j in range(n):
        rotated[i][j]=x[n-j-1][i]
```
- 왼쪽으로 90도 회전
    - 원래 행렬의 행이 바뀐 행렬의 열이 된다
    - 원래 행렬의 i열 회전시킬 경우 바뀐 행렬의 행은  `n-i-1`
```python
x=[[1,2,3],
   [4,5,6]
   [7,8,9]]
# 왼쪽 회전
x=[[3,6,9],
   [2,5,8],
   [1,4,7]]
rotated=[[0]*n for _ in range(n)]
for i in range (m):
    for j in range(n):
        rotated[i][j]=x[j][n-i-1]
```
