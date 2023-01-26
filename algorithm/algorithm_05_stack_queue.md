# 스택(stack)
- 쌓는다는 의미, 데이터를 한 쪽에서만 넣고 뺀다 즉 , `LIFO` **후입선출**방식이다
- 스택자료의 데이터 삽입행위 `psuh` , 데이터를 가져오는 행위`pop`
- 홈페이지의 뒤로가기 =가장 최근의 페이지 가져오는 일종의`stack` 예시
- 괄호 매칭, 함수 호출(재귀 호출), 백트래킹 DFS(깊이 우선 탐색)에 사용
- 파이썬은 리스트로 스택 간편하게 사용 가능
```python
#백준 zero 문제 10773 
import sys
K=int(sys.stdin.readline().strip())
ans=[]
for i in range(K):
    x=int(sys.stdin.readline().strip())
    if x==0:
        ans.pop()
    else:
        ans.append(x)
print(sum(ans))
```

# 큐(queue)
- 한쪽 끝에서 데이터 넣고 다른 한쪽에서만 데이터를 뺄 수 있는 자료구조,`FIFO` **선입선출** 방식
- 순서문제, 대기문제를 해결할 때 사용한다
- 프로세스 관리, 클라이언트/서버 관리에 사용
- 알고리즘 문제 해결에는 BFS(너비 우선 탐색),다익스트라(우선순위 큐)
- 큐는 데이터를 뺄 때 데이터가 많은 경우 비효율적(리스트의 인덱스 하나씩 당겨진다)
- `deque`, 덱 자료구조는 양방향으로 자료 삽입과 삭제 자유롭다
<img width="512" alt="덱의 삽입,추출" src="https://user-images.githubusercontent.com/118239192/214808543-2fa5610c-1822-4b65-93cd-9b0bea735959.png">
