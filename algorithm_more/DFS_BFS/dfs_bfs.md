# DFS와 BFS
- 탐색 : 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
- DFS와 BFS가 대표적인 탐색 알고리즘이다

## 기초 개념인 자료구조 기초와 재귀함수 
- 스택: 선입후출,후입선출의 구조 , 파이썬에서는 리스트 형태 사용 append 와 pop 메서드를 이용하여 스택 자료구조와 동일하게 동작한다.
- 큐 : 선입선출의 구조, 파이썬에서는 `collections`에서 `deque` 자료구조를 활용하여 사용 

- 재귀함수 : 자기 자신을 다시 호출하는 함수  (컴퓨터 내부에서 재귀함수 사용시 스택 자료구조를 이용한다 )
    - 재귀함수의 종료 조건: 재귀함수 사용 시 `종료조건`을 반드시 명시해야 한다 (무한 호출 될 수 있기 때문)
```python
m=int(input())
def factorial(n):
    if n<=1:
        return 1
    return n * factorial(n-1)
print(factorial(m))
# 재귀함수의 대표적인 예시가 팩토리얼이다

```

## DFS
- Depth-First Search, 깊이 우선 탐색이라고도 하며 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
- 그래프는 노드와 간선으로 표현
- 인접행렬과 인접 리스트를 이용하여 그래프 표현 후 DFS 탐색 가능 (기초 그래프 개념은 `algorithm 폴더 -algorithm_10_graph`참고)
- DFS의 구체적인 동작 과정
    1. 탐색 시작 노드를 스택에 삽입하고 방문처리를 한다
    2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다. 방문하지 않은 인접 노드가
     없으면 스택에서 최상단 노드를 꺼낸다
    3. 2번의 과정을 수행할 수 없을때 까지 반복한다 
```python
def dfs(graph, v,visited):
    visited[v]=True
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,,visited)

```
- DFS를 재귀함수로 사용 할 경우 더 느려지는 경우가 있어 재귀함수를 사용하지 않고 stack을 사용한 DFS를 구현하기도 한다
```python
def dfs(start):
    stack=[start]
    visited[start]=True # 시작점은 방문으로 바꾼다
    while stack:        # stack이 빌때까지 탐색
        cur=stack.pop()
        for adj in graph[cur]:
            if not visited [adj]:
                print(adj)  
                visited[adj]=True
                stack.append(adj)

graph=[[1,2],[0,3,4],[0,4,5],[1],[1,2,6],[2],[4]]
visited=[False]*7 # 방문 체크리스트
dfs(0)
```


## BFS (너비우선탐색 알고리즘)
- 가까운 노드부터 탐색하는 알고리즘 
- BFS 구현에서는 선입선출 방식인 큐 자료구조를 이용하는 것이 정석
- 동작 과정
    1. 탐색 시작 노드를 큐에 삽입하고 방문처리
    2. 큐에서 노드를 꺼내 해낭 노드의 인접 노드 중 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리 
    3. 2번 과정을 수행할 수 없을 때 까지 반복한다 
```python
from collections import deque

def bfs(graph,start,visited):
    # 큐 구현을 통하여 deque를 사용한다
    queue=deque([start])
    
    visited[start]=True
    # 현재 노드 방문 처리
    while queue :#queue가 빌때까지 반복한다 
        v=queue.popleft()
        print(v,end=' ')
        # 해당 노드와 연결된 방문하지 않은 노드들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                visited[i]=True
                queue.append(i)
graph=[[],
       [2,3,8],
       [1,7],
       [1,4,5],
       [3,5],
       [3,4],
       [7],
       [2,6,8],
       [1,7]]

visited=[False]*9

bfs(graph,1,visited)
```