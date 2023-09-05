import sys
import heapq
input = sys.stdin.readline
n , m = map(int, input().split())
inf= int(1e9)
distance= [inf] * (n + 1)
distance[0] = 0
graph= [[] for _ in range (n+1)]
for i in range (m):
    a, b = map(int, input().split())
    graph[a].append((1, b))
    graph[b].append((1,a))
def dijkstra (graph):
    q = []
    distance[1] = 0
    heapq.heappush(q, (0, 1))
    while q:
        cost, now = heapq.heappop(q)
        if cost > distance[now] :
            continue
        for i in graph[now]:
            next_cost = cost + i[0]
            if next_cost < distance[i[1]]:
                distance[i[1]] = next_cost
                heapq.heappush(q, (next_cost, i[1]))
    return distance
distance = dijkstra(graph)
print(distance)
max_d= max(distance) # 무조건 연결 가능하니까 max 써도 괜찮음
print(distance.index(max_d), end= ' ')
print(max_d, end= ' ')
print(distance.count(max_d))
