# 최단 경로 알고리즘
- 최단 경로 알고리즘: 가장 짧은 경로를 찾는 알고리즘 (길 찾기 문제)
- 대부분의 경우 그래프로 문제를 해결한다
- 크게 `다익스트라 알고리즘` ,`플로이드 워셜 알고리즘` , 벨만 포드 알고리즘이 있다

## 다익스트라 최단 경로 알고리즘
- 그래프에서 여러개의 노드가 있을 때 특정한 노드에서 출발 하여 다른 노드로 가는 최단경로를 구해주는 알고리즘 
- GPS소프트웨어의 기본 알고리즘으로 채택 되기도 한다
- 다익스트라 알고리즘의 기본 원리
    1. 출발 노드를 설정
    2. 최단 거리 테이블  초기화
    3. 방문하지 않은 노드 중에서 최단거리가 가장 짧은 노드 선택
    4. 해당 노드를 거쳐 다른 노드로 가는 비용 계산, 최단 거리 테이블 갱신
    5. 3번과 4번 과정을 반복
- 다익스트라 알고리즘은 매번 현재 처리하고 있는 노드를 기준으로 주변 간선을 확인한다. 
- 다익스트라 알고리즘의 경우 구현하기 쉬운 느린 코드, `구현하기 까다롭지만 빠르게 동작하는 코드`가 있다 , 두 번째 코드가 반드시 숙달 될 필요가 있다.
- 다익스트라 알고리즘은 한 단계당 `하나의 노드에 대한 최단거리`를 확실히 찾는 것이다. (그렇기 때문에 마지막 노드에서는 더이상 테이블이 갱신 될 수 없다 )
- 다익스트라 알고리즘의 시간복잡도는 O(V^2)이다. (V는 노드의 개수)
- 처음에 각 노드에 대한 최단거리를 담는 1차원 리스트를 선언  => 이후 단계마다 방문X 노드 중 최단거리 가장 짧은 노드 선택위해 1차원 리스트의 모든 원소를 순차탐색한다 
```python
# 간단한 다익스트라 알고리즘

import sys
input = sys.stdin.readline
inf = int(1e9) # 무한한 크기라고 가정

# 노드의 개수와 간선의 개수를 입력받는다
n , m = map(int,input().split())

# 시작 노드 번호를 입력받는다
start = int(input())
# 각 노드에 대해 연결되어 있는 리스트를 만들기
graph = [[] for _ in range(n+1)]
# 방문처리할 리스트
visited = [False] * ( n + 1)
# 최단거리 테이블을 생성, 초기에는 전부 무한으로 
distance = [inf] * ( n + 1)
# 노드번호와 비용을 입력받는다 a번 노드에서 b 노드 까지의 비용(거리)가 c이다
for _ in range (m):
    a, b, c =map(int,input().split())
    graph[a].append((b,c))

#다익스트라 알고리즘을 사용하기 위해선 방문하지 않은 노드 중 최단거리가 가장 짧은 노드를 선택해야 한다 

def choose_smallest_node():
    min_value = inf
    index = 0 # 가장 짧은 노드를 선택해야 하니까 초기 값 설정
    for i in range (1, n + 1): 
        if distance[i]<min_value and not visited[i] :
            index=i
            min_value=distance[i]
    return index

## 
def dijkstra(start):
    # 시작 노드에 대해서 초기화 거리 0, 방문처리
    distance[start]=0
    visited[start]=True
    
    # 그래프안에 (노드, 비용/거리) 로 표시되어있기 때문에 0번 인덱스가 노드 ,1번 인덱스가 거리 즉 distance[노드]= 거리 라는 식이다 
    for j in graph[start]:
        distance[j[0]]=j[1]
    
    # 시작 노드를 제외한 n-1개의 노드에 대해서 짧은 노드 선택, 연결 확인, 더 짧은 거리 발견하면 갱신
    for i in range(n - 1):
        # 시작노드에서 가장 거리가 짧은 노드 선택 위에서 방문처리, for문에서 거리 표시 처리 한거 때문에 구할 수 있다.
        now = choose_smallest_node()
        # 짧은노드에서부터 다시 시작
        visited[now] = True # 방문처리
        
        # 이 노드에서 연결된 다른 노드 확인 즉 now가 짧은 노드로 선택되고 그에 연결된 k노드까지의 거리를 더한것이 거리 후보
        # k는 현재 (노드, 거리)의 튜플 형태
        for k in graph[now]:
            cost = distance[now] + k[1]
            if cost < distance[k[0]]:
                distance[k[0]] = cost

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1,n+1):
    if distance[i] == inf:
        print("fail")
    else:
        print(distance[i])
```
- 위 코드의 시간복잡도는 O(V^2)이다. 총 O(V)번에 걸쳐 최단 거리가 가장 짧은 노드를 선형 탐색하고 ,현재노드와 연결된 노드를 확인해야 하기 때문이다. 
- 노드개수가 5000 개 이하면 문제가 되진 않지만 이상일 경우 개선된 다 익스트라 알고리즘을 사용할 필요가 있다.


## 개선된 다익스트라 알고리즘
- 개선된 다익스트라 알고리즘의 최악의 경우의 시간 복잡도는 `O(ElogV)` 이다 (V는 노드개수, E는 간선의 개수)
- 최단 거리가 가장 짧은 노드를 탐색하는 과정을 줄인다.
- Heap 자료구조를 이용한다.
- `힙`
     - 힙 자료구조는 우선순위 큐를 구현하기 위해 사용하는 자료구조 중 하나이다.
     - PriorityQueue 혹은 heapq를 사용하여 우선순위 큐를 만들 수 있다. 
     - 우선순위 값을 표현할 때는 일반적으로 정수형 자료형의 변수가 사용된다. 
     - 우선순위 큐를 구현할 때는 내부적으로 최소 힙 혹은 최대 힙을 이용한다
     - 최소힙은 값이 낮은 데이터가 먼저 삭제, 최대 힙은 값이 큰 데이터가 먼저 삭제된다. 
     - 다익스트라 최단 경로 알고리즘의 경우 비용이 적은 노드를 우선 방문하므로 최소힙 구조가 적합하다 (파이썬 라이브러리가 최소힙 구조) 
     - <`Tip` = 최소 힙을 최대 힙처럼 사용하고 싶을 경우 우선순위에 해당하는 값에 음수부호를 붙여서 넣었다가 , 나중에 우선순위 큐에서 꺼낸 다음 음수부호를 다시 붙여 원래 값으로 돌리는 방식을 사용할 수 있다.>
     - 우선순위 큐를 리스트로 구현할 경우와 힙으로 구현할 경우
        - 리스트: 삽입시간의 시간복잡도는 O(1)이지만, 삭제시간은 O(N)
        - 우선순위 큐: 삽입시간과 삭제시간의 시간복잡도 모두 `O(logN)`
    
- 우선순위 큐를 이용한 개선된 다익스트라 알고리즘의 순서는 p.242 부터 책으로 공부  
```python

import sys
import heapq
input= sys.stdin.readline
inf=int(1e9)

# 기본 정보 입력 받기  

n , m = map(int,input().split())
start= int(input())
graph=[[] for _ in range(n+1)]
distance=[inf] * (n + 1)

for i in range(m):
    a, b, c= map(int,input().split())
    graph[a].append((b,c))

# 다익스트라 알고리즘 정의
def dijkstra(start):
    q=[] #우선순위 큐를 만들기 위해 빈 리스트 생성
    #출발 노드를 우선순위 큐에 삽입해야 한다
    heapq.heappush( q ,(0,start) )

    # 출발노드까지 거리가 0이라는걸 distance 리스트에서도 삽입
    distance[start]=0
    
    # 힙큐가 비어있지 않다면
    while q :
        # 거리, 비용 형태로 현재 
        dist, now = heapq.heappop(q)
        # 후에 같은 노드에 대해 거리가 여러개인 우선순위 큐가 있을 것이다 . 현재 distance는 더 짧게 기록되있지만 우선순위큐는 길 수 있다
        # 따라서 우선수위 큐에서 나온 거리가 distance보다 길다면 무시할 수 있는 것이다. 이미 처리했기 때문
        if distance[now] <dist:
            continue #다음 큐로 진행
        # 이제 큐에서 꺼낸 노드와 연결된 노드들로 확장
        for i in graph[now]:
            cost= dist + i[1] #우선순위 큐에 기록된 노드까지의 거리 + 자기 거리 더한 것와 현재 기록되어있는 거리를 비교해야한다 
            # 만약 갱신한다면 갱신 한 노드에 대해서 우선순위 큐에 삽입되어야 한다 
            if cost < distance[i[0]]:
                distance[i[0]]= cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

for i in range( 1, n+1):
    if distance[i]==inf:
        print('fail')
    else:
        print(distance[i])
```
- 개선된 다익스트라 알고리즘은 E개의 간선을 heap에서 넣었다 빼는 과정으로 힙에 N개의 데이터를 넣었다 빼는 과정의 시간복잡도는 O(NlogN)이다
- 즉 O(ElogE)인데 간선과 노드의 입장에서 간선은 항상 `E< V^2 ` 이며 log를 씌우면 log E < 2 log V 이다
- 따라서 O(ElogE)의 시간복잡도는 대략적으로 O(ElogV)와 같다고 볼 수 있다 

# 플로이드 워셜 알고리즘
- 다익스트라 알고리즘은 한 지점에서 다른 특정지점까지의 최단 경로를 구해야 하는 경우 사용
- 모든 지점에서 다른 모든 지점까지의 최단 경로를 구해야 할 때 사용하는 알고리즘이 `플로이드 워셜 알고리즘`
- 다익스트라 알고리즘 처럼 플로이드 워셜 알고리즘 역시 단계마다 `거쳐가는 노드` 를 기준으로 알고리즘을 수행한다.
- 노드의 개수가 N개 일때 알고리즘 상으로 N번의 단계를 수행한다, 단계마다 O(N^2)의 연산을 하므로 총 O(N^3)의 시간복잡도를 가진다 
- 현재 확인하고 있는 노드를 제외하고 N-1개의 노드중에서 서로 다른 노드 (a,b) 쌍을 선택한 후 거리를 갱신한다 
- n-1 P 2 의 시간복잡도이고 대략적으로 O(N^2)이다 
- 구체적인 점화식은 다음과 같다

![image](https://github.com/ShinWooHyeon/TIL/assets/118239192/f33316d1-cf3f-4ef1-a9d1-766d96c2c9ed)

```python
inf=int(1e9)

#노드와 간선 입력 받기

n = int(input())
m = int(input())

# 2차원 리스트를 만들고 모든 값을 무한으로 초기화
graph = [[inf]*(n+1) for _ in range(n+1)]

# 자기자신에서 자기로 가는 값은 모두 0으로 초기화

for i in range(1, n+1):
    graph[i][i]=0

# 각 간선에대한 정보를 입력받아 그 값으로 변경

for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a][b]=c

# 점화식에 따라 플로이드 워셜 알고리즘 수행

for i in range (1, n+1):
    for j in range (1, n+1):
        for k in range(1, n+1):
            graph[j][k]=min(graph[j][i]+graph[i][k],graph[j][k])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b]==inf:
            print("inf",end=' ')
        else:
            print(graph[a][b], end=' ')
    print()

```