# 중요 알고리즘 정리
- 브루트 포스와 그리디 알고리즘은 for문, 아이디어 느낌이기 때문에 생략한다.
- 주요 알고리즘인 DFS, BFS , 이진탐색, 그래프 이론(union- find), 최단경로 알고리즘에 대해서 일단 정리한다
## DFS 알고리즘 (깊이 우선 탐색 알고리즘)
- Depth- first search 알고리즘 - 후입선출의 느낌
- 구체적인 동작 과정
    1. 탐색 시작 노드를 스택에 삽입하고, 방문처리를 한다 .
    2. 스택의 최상단 노드에 방문하지 않은 인접노드가 있으면 그 인접노드륵 스택에 넣고, 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드 꺼낸다
    3. 2번 과정을 방문할 수 없을때 까지 반복한다

```python
def dfs (start) :
    stack = [start]
    visited[start] = True
    while stack :
        cur = stack.pop()
        for adj in  graph[cur]:
            if not visited[adj]:
                # 방문 순서 보고싶으면
                print(adj)
                visited[adj] = True
                stack.append(adj)  

```

## BFS 알고리즘 (너비 우선 탐색 알고리즘)
- 가까운 노드부터 탐색하는 알고리즘 
- 선입선출 방식의 큐 자료구조를 이용한다 
- 동작과정
    1. 탐색 시작 노드를 큐에 삽입하고 방문처리
    2. 큐에서 노드를 꺼내고 해당노드의 인접한 노드 중 방문하지 않은 노드를 큐에 삽입
    3. 2번 과정 수행할 수 없을때 까지 반복한다. 
```python
from collections import deque
def bfs (graph, start, visited):
    queue=deque([start])
    visited[start] = True
    # 선입 선출이 되려면 popleft를 진행해야한다 
    while queue :
        v= queue.popleft()
        for i in graph[v]:
            if not vsiited[i]:
                visited[i] = True
                queue.append(i)
```

## DFS 알고리즘을 이용한 조합 문제 풀이
- XX중 



# 이진탐색 알고리즘 
- 완전 탐색 (순차탐색) 알고리즘의 시간 복잡도는 O(N)
- 이진탐색 알고리즘은 O(logN)
```python
def binary_search(array, target, start, end):
    if start > end : 
        return None
    
    mid = (start +end)//2
    if array[mid] == target :
        return mid
    if array[mid] > target :
        return binary_search(array, target, start, mid - 1)
    if array[mid] < target :
        return binary_search(array, target, mid + 1, end)
    
## 반복문 이용 이진탐색
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end)//2
        if array[mid] == target :
            return mid 
        if array[mid] > target :
            end = mid -1
        if array[mid] < target :
            start = mid + 1

```

# 그래프 이론 
- 대표적인 그래프 이론에는 union-find(서로소 집합), 크루스칼 알고리즘이 있다
## Union- find (서로소 집합)
- 서로소 집합 = 공통 원소가 없는 두 집합
- 서로조 집합 자료구조 = `서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조`
- 서로조 집합 자료구조는 `union (합집합)` 연산과 `find (찾기)` 연산으로 조작가능하다
```python
# find 연산
def find_parent(parent, x) :
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

# union 연산
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

v, e = map(int ,input().split())
parent = [0] * (v + 1)

for i in range (1, v + 1):
    parent[i] = i
# 노드별로 연결되어 있으므로 union 연산
for i in range (e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)
# 각 원소가 속한 집합 출력
for i in range (1, v+1):
    print(find_parent(parent,i), end=' ')

print()
# 부모 테이블 출력
for i in range (1, v+1):
    print(parent[i],end=' ')
```
## 크루스칼 알고리즘
- union - find 연산을 통해 사이클이 발생되었는지 (두 부모가 같아져 순환 발생)
- 최소 신장 트리를 만들어내는 알고리즘이 크루스칼 알고리즘이다 
- 최소신장 트리는 일종의 트리 자료구조로 간선 개수가 노드 -1 이다
- 크루스칼 알고리즘의 동작 순서
     1. 간선 데이터를 비용에 따라 `오름차순` 정렬 
     2. 간선 확인하며 사이클 발생시키는지 확인하고 사이클이 발생하지 않을 경우 최소 신장 트리에 포함시킨다
     3. 모든 간선에 2번 과정을 반복한다 
```python
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x] 

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

# 노드의 개수와 간선의 개수를 입력 받아야 한다
v, e = map(int ,input().split())
for i in range (1, v+1) :
    parent[i] = i

# 간선을 담을 리스트와 비용 총 합 계산할 변수
nodes = []
result = 0

for i in range (e):
    a, b, cost = map(int, input().split())
    nodes.append((cost, a, b))
# 비용 정렬
nodes.sort()

for node in nodes :
    cost, a, b = node
    if find_parent(parent, a) != find_parent(parent, b) :
        union_parent(a, b)
        result += cost
    

```

# 위상정렬 
- 순서가 정해져 있는 일련의 작업을 수행할 때 사용
- 위상정렬 알고리즘의 수행 순서는 다음과 같다
1. 진입차수가 0인 노드를 큐에 넣는다
2. 큐가 빌 때 까지 다음 과정을 반복한다
    - 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다. (연결된 노드들의 진입차수가 하나씩 줄게 된다)
    - 새롭게 진입차수가 0이 된 노드들을 큐에 삽입한다.
- 모든 원소 방문 전에 큐가 빈다면 사이클이 존재한다고 할 수 있다 .여기서는 일단 사이클이 존재하지 않는다고 가정
```python
from collections import deque
# 노드의 개수와 간선의 수를 입력받는다
v, e = map(int, input().split())

# 모든 노드에 대해서 진입차수는 일단 0으로 계산
indegree = [0] * (v + 1)

graph = [[] for _ in range (v+1)]
# 그래프를 입력받으며 진입차수를 증가시킨다
for i in range (e):
    a, b = map(int ,input().split())
    graph[a].append(b)
    indegree[b] += 1

# 위상정렬 함수 정의 
def topology_sort():
    # 결과 담을 리스트 (순서)
    result = []
    q = deque()
    for i in range (1, v+1):
        if indegree[i] == 0:
            q.append(i)
    # 큐에서 뽑아내면서 순서 
    while q:
        now = q.popleft()
        result.append(now)
        for node in graph[now]:
            indegree[node] -= 1 
            if indegree[node] == 0:
                q.append(node)


```

# 최단경로 알고리즘 (다익스트라, 플로이드 워셜) 
## 다익스트라 알고리즘
- 그래프의 여러개의 노드가 있을 때 특정 노드에서 다른 노드로 가는 최단경로 구하는 알고리즘 
- 다익스트라 알고리즘의 수행 순서 
- 우선순위 큐를 사용하여 (heap) 노드 탐색 과정으 줄인다.(우선순위 큐의삽입시간과 삭제시간의 시간 복잡도는 모두 O(logN))
    1. 출발 노드를 설정한다
    2. 최단 거리 테이블을 초기화 한다 
    3. 방문 하지 않은 노드 중에서 최단거리가 가장 짧은 노드를 선택한다
    4. 해당 노드를 거쳐 다른 노드로가는 비용을 계산하고, 최단 거리 테이블을 갱신한다
    5. 3번과 4번 과정을 반복한다 

```python
import heapq
import sys
input = sys.stdin.readline
inf = int(1e9)

# 기본 정보를 입력받는다 노드의 수, 간선의 수 ,출발점
n, m = map(int, input().split())
start = int(input())

# 최단거리 계산 => 거리 리스트와, 입력받을 그래프 초기 설정
graph = [[] for _ in range(n + 1)]
distance = [inf] * (n + 1) 

# 그래프를 입력받는다
for i in range (m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, c)) 

# 다익스트라 알고리즘을 수행한다 
def dijkstra(start):
    q = []
    # 출발노드의 거리, 비용은 0이고 우선순위 큐에 삽입한다
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        # 현재 위치를 큐에서 팝한다
        dist, now = heapq.heappop(q)
        
        # 갱신이 이미 되서 힙에 있는 dist보다 distance가 작다면 이 노드(큐)는 스킵
        if distance[now] < dist:
            continue 
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                # 갱신하고 힙큐에 삽입 
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

```

## 플루이드 워셜 알고리즘 
- 다익스트라 알고리즘은 한 지점에서 다른 특정지점까지의 최단 경로를 구해야 하는 경우 사용
- 모든 지점에서 다른 모든 지점까지의 최단 경로를 구해야 할 때 사용하는 알고리즘이 `플로이드 워셜 알고리즘`
- N^3의 시간복잡도를 가진다
```python
inf = int(1e9)
# 노드의 수와 간선 수 입력받기
n , m = map(int ,input().split())

graph = [[inf] * (n + 1) for _ in range (n + 1)]

# 자기자신으로 가는 거리는 0
for i in range (1, n + 1):
    graph[i][i] = 0


# 그래프 입력받기 양쪽 연결 있으면 b,a 도 고려해야한다 
for i in range (m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for i in range (1, n+1) :
    for j in range (1, n + 1):
        for k in range (1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
```

