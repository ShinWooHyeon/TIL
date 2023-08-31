# 그래프 이론
- 그래프의와 트리는 다음과 같은 차이를 보인다.
![image](https://github.com/ShinWooHyeon/TIL/assets/118239192/fde702d7-b0d4-4fb0-a1d6-06ffc3b8bb37)

- 그래프의 구현 방법은 2가지 방식이 존재한다
    - 인접 행렬: 2차원 배열을 사용하는 방식
    - 인접 리스트: 리스틀 사용하는 방식
- 노드의 개수가 V 간선의 개수가 E 라면 인접행렬은 O(V^2)의 메모리 공간이 필요 , 인접리스트는 O(E)만큼의 메모리 공간만 필요
- 인접행렬은 특정한 노드에서 특정한 노드까지의 비용을 O(1)로 알 수 있는 반면 인접리스트는 O(V) 만큼의 시간 소요 
- 다익스트라 알고리즘이 인접리스트, 플로이드 워셜 알고리즘이 인접행렬을 사용한다.

# 다양한 그래프 알고리즘

## 서로소 집합
- 서로소 집합 = 공통 원소가 없는 두 집합
- 서로조 집합 자료구조 = `서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조`
- 서로조 집합 자료구조는 `union (합집합)` 연산과 `find (찾기)` 연산으로 조작가능하다

### 서로소 집합 자료구조
- 트리 자료구조를 이용하여 서로소 집합 자료구조를 표현한다. 
- 서로소 집합 계산 알고리즘은 다음과 같다
    - 1. union (합집합) 연산을 확인하여 서로 연결된 두 노드 A, B를 확인한다.
        - (1).  A와 B의 루트 노드 A' 과 B'을 찾는다
        - (2).  A'를 B'의 부모노드로 설정한다 (B' 가 A'를 가리키도록 한다)
    - 2. 모든 union 연산을 처리할 때 까지 1번 과정을 반복한다.
- 이러한 union 연산은 그래프로 표현될 수 있다. 
- union 연산을 효과적으로 수행하기 위해서는 `부모 테이블`이 필요하다. 또한 루트노드를 계산하기 위해서는 부모테이블을 확인 후 거슬러 올라가야 한다.
(자신의 부모 노드가 부모 노드가 있을 경우 루트노드가 아니기 때문에)
- 즉 , 서로소 집합 알고리즘으로 루트노드를 찾기 위해서는 재귀적으로 부모를 거슬러 올라갸아 한다.
```python
# 부모 테이블을 계속 이용하는 것을 알 수 있다
# 특정 원소가 속한 집합을 찾기 (find)
def find_parent( parent , x):
    #루트 노드가 아니라면 루트 노드를 찾을 때 까지 반복한다
    if parent[x] !=x: # x의 부모가 x가 아니라면 , 즉 x가 루트노드가 아니라면
        return find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기 (union)

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선 개수(union 연산 개수) 입력받기
v, e = map(int,input().split())
parent=[0] * (v+1) #부모테이블을 일단 다 0으로 만들고

# 자기자신을 부모테이블에 부모로 전부 넣어야한다
for i in range (1, v+1):
    parent[i] = i

# union 연산을 수행한다 , 부모테이블만 알 뿐 아직은 루트노드를 알 수 없다
for i in range (e) :
    a , b = map(int,input().split())
    union_parent (parent, a, b)

# 각 원소가 속한 집합 출력
for i in range (1, v+1):
    print(find_parent(parent,i), end=' ')

print()
# 부모 테이블 출력
for i in range (1, v+1):
    print(parent[i],end=' ')
```
- 그러나 위 경우 find 함수의 시간복잡도가 O(V)가 될 수 있다 (루트노드 찾으므로 )
- 따라서 find 함수에서 재귀함수를 돌면서 부모 테이블 값을 갱신한다면 경로압축을 할 수 있다
```python
# 경로압축코드만 따로 보면

def find_parent( parent , x):
    #루트 노드가 아니라면 루트 노드를 찾을 때 까지 반복한다
    if parent[x] !=x: # x의 부모가 x가 아니라면 , 즉 x가 루트노드가 아니라면 x의 부모노드의 부모노드를 x의 부모노드로 설정한다 
        return find_parent(parent, parent[x])
    return parent[x]
```
- 원소가 속한 집합을 찾는 시간복잡도느 노드 V-1개의 union 연산 M개의 find 연산 => V+M*logV
- 서로소 집합을 사용할 경우 사이클을 판별 할 수 있다
#### 서로소 집합을 활용한 사이클 판별
- union 연산 (간선)을 하나씩 확인하면서 사이클을 판별 할 수 있다.
- 순서
    1. 각 각선(union)을 확인하며 두 노드의 루트노드 확인 
        - 루트노드가 다르다면 union 연산
        - 루토느드가 같다면 사이클 발생
    2. 그래프의 모든 간선에 대하여 1번 과정 반복 

```python
def find_parent( parent , x):
    #루트 노드가 아니라면 루트 노드를 찾을 때 까지 반복한다
    if parent[x] !=x: # x의 부모가 x가 아니라면 , 즉 x가 루트노드가 아니라면
        return parent[x]= find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기 (union)

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선 개수(union 연산 개수) 입력받기
v, e = map(int,input().split())
parent=[0] * (v+1) #부모테이블을 일단 다 0으로 만들고

# 자기자신을 부모테이블에 부모로 전부 넣어야한다
for i in range (1, v+1):
    parent[i] = i

cycle =False
# union 연산을 수행한다 , 이때 사이클을 확인한다  사이클이 발생했을 경우 union을 하지 않는다 
for i in range (e) :
    a , b = map(int,input().split())
    # 사이클 발생시 종료 
    # 부모노드가 자기자신인애와 union 할 경우?는 처음경우에는 사이클이 발생 안한다 부모노드가 서로 달라서  
    if find_parent(parent, a) == find_parent(parent, b):
        cycle=True
        break
    else:
        union_parent (parent, a, b)

if cycle:
    print("cycle 발생")
else:
    print("cycle 발생x")

```

## 신장 트리
- 그래프 알고리즘에 자주 출제되는 문제 
- 하나의 그래프가 있을 때 모든 노드를 포함하면서 `사이클이 존재하지 않는 부분 그래프`

### 크루스칼 알고리즘
- 최소한의 비용으로 신장 트리를 찾아야 할 필요가 종종 있다. 
- 도시 3개를 모두 연결되게 하고 싶을 때 최소한의 비용으로 연결하는 방법과 같은 문제에서 사용 
- `크루스칼 알고리즘` = 최소 신장 트리 알고리즘 
- 일종의 그리디 알고리즘과 유사하다
- 크루스칼 알고리즘의 순서
    - 1. 간선 데이터를 비용에 따라 오름차순으로 정렬한다
    - 2. 간선을 하나씩 확인하며 사이클을 발생시키는지 확인한다 .
        - (1) . 사이클이 발생하지 않을 경우 최소 신장트리에 포함시킨다
        - (2) . 사이클이 발생하는 경우 최소 신장트리에 포함시키지 않는다.
    - 3. 모든 간선에 2번 과정을 반복한다ㅏ.
- 최소 신장 트리는 일종의 트리 자료구조로 간선의 개수가 노드 -1 이다 

```python
def find_parent( parent , x):
    #루트 노드가 아니라면 루트 노드를 찾을 때 까지 반복한다
    if parent[x] !=x: # x의 부모가 x가 아니라면 , 즉 x가 루트노드가 아니라면
        parent[x]= find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기 (union)

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선 개수(union 연산 개수) 입력받기
v, e = map(int,input().split())
parent=[0] * (v+1) #부모테이블을 일단 다 0으로 만들고

# 간선을 담을 리스트와 비용을 담을 변수 설정
nodes=[]
result=0

# 자기자신을 부모테이블에 부모로 전부 넣어야한다
for i in range (1, v+1):
    parent[i] = i
#간선에 대한 정보 입력 받기  (비용까지)
for i in range (e) :
    a, b , cost= map(int,input().split())
    nodes.append((cost, a, b)) # cost 순으로 정렬하기 위해서

#비용순 정렬
nodes.sort()

for i in nodes:
    cost, a, b= i
    # union할 노드들의 사이클을 확인후 사이클이 발생하지 않으면 union 하고 비용을 추가한다
    if find_parent(parent, a) !=find_parent(parent, b):
        union_parent(parent,a,b)
        result+=cost

print(result)
```
- 크루스칼 알고리즈은 간선의 개수가 E 일때 O(ElogE)의 시간복잡도를 가진다. 간선의 개수를 정렬하는 작업의 시간복잡도( 서로소 알고리즘의 시간복잡도는 작으므로 무시 가능하다)

### 위상정렬
- 위상정렬이란 순서가 정해져 있는 일련의 작업을 수행할 때 사용할 수 있는 알고리즘이다.
- 즉, `방향 그래프의 모든 노드를 방향성에 거스르지 않도록 나열하는 것` 
- 진입차수: 특정한 노드로 들어오는 간선의 개수 
- 위상정렬 알고리즘의 순서는 다음과 같다
    - 1. 진입차수가 0인 노드를 큐에 넣는다
    - 2. 큐가 빌때까지 다음의 과정을 반복한다
        - (1). 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다.
        - (2). 새롭게 진입차수가 0이 된 노드를 큐에 넣는다
- 모든 원소 방문전에 큐가 빈다면 사이클이 존재한다고 판단할 수 있다 (이후 추가학습) ,여기서는 일단 사이클이 존재하지 않는다고 가정

```python
from collections import deque

#노드의 개수와 간선 입력받고
v, e = map(int, input().split())

# 모든 노드에 대한 진입차수는 0으로 초기화 
indegree=[0]* (v+1)

# 간선 정보 입력받기 위한 리스트
graph=[[] for _ in range(v+1)]

# 간선 정보 입력받기 (진입차수는 받는 차수 즉 도착지점의 개수만큼 증가한다)
for _ in range (e):
    a, b = map(int, input().split())
    # a->b
    graph[a].append(b)
    # 진입차수 증가
    indegree[b]+=1

# 위상정렬함수 정의
def topology_sort():
    result = [] # 결과 담을 리스트
    q = deque()

    # 진입차수가 0인 노드를 큐에 삽입한다
    for i in range(1, v+1):
        if indegree[i]==0:
            q.append(i)
    
    # 큐가 빌 때까지 반복한다
    while q:
        #큐에서 원소 꺼내기
        now= q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i]-=1
            # 새롭게 삽입
            if indegree[i]==0:
                q.append(i)
    
    #위상 정렬 결과 출력
    for i in result :
        print(i, end=' ')
topology_sort()
```
- 위상정렬의 시간복잡도는 O(V+E) 이다 모든 노드를 한 번씩 확인하고 (result에 넣는거), 간선을 모두 제거 (E) 하기 때문
