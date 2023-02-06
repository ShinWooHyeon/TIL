# 그래프 탐색 알고리즘
- 그래프탐색 알고리즘
    - DFS(깊이우선탐색): 그래프의 깊이를 우선탐색하기 위해 스택 활용
    - BFS(너비우선탐색): 그래프의 너비를 우선탐색하기 위해 큐를 활용

# DFS (깊이우선탐색 알고리즘)
- 시작 정점에서 시작 가장 하위 정점까지 깊게 탐색 (일종의 미로,막히면 다시 돌아와서 탐색)
- 동작 과정
    - 각 정점 방문했는지를 판별한 `visit check` 필요
    - 순서
    1. 정점 방문처리 및 스택에 값 삽입
    2. 스택 마지막 값을 꺼내고 인접한 정점들을 확인한다
    3. 방문하지 않은 인접 정점을 다시 1번으로 돌아가는 반복문 (다 방문할 때 까지)
```py
graph=[[1,2],[0,3,4],[0,4,5],[1],[1,2,6],[2],[4]]
visited=[False]*7 # 방문 체크리스트
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
dfs(0)
```