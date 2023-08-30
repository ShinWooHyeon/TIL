# 미래도시
import sys
import heapq

input = sys.stdin.readline
inf  = int(1e9)
# 회사의 개수와 경로의 개수 받고
n , m = map(int,input().split())
distance=[inf] * (n+1)

# 경로를 입력받는다

graph=[[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))
# 거쳐가는 회사와 도착할 회사의 번호를 입력받는다
x , k = map(int,input().split())

def dijkstra (start):
    q=[]
    distance[start]=0
    heapq.heappush(q,(0,start))
    
    while q:
        dist, now =heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost= dist + i[1]
            if distance[i[0]]> cost:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(1)
a=distance[k]

distance=[inf] * (n+1)
dijkstra(k)
b=distance[x]

