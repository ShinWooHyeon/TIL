# 전보
import heapq
import sys
n, m, s = map(int,input().split())
inf = int(1e9)
distance= [inf] * (n+1)


graph=[[] for _ in range (n+1)]

for i in range (m):
    a, b, c = map (int,input().split())
    graph[a].append((b,c))

def dijkstra (start):
    q=[]
    distance[start]=0
    heapq.heappush(q,(0,start))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost= dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(s)
cnt=0
max_time=0
for i in distance:
    if i!=inf and i!=0:
        cnt+=1
        if i>max_time:
            max_time=i
print(cnt, end=' ')
print(max_time)
