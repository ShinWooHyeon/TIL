# 화성탐사
import heapq
import sys
input = sys.stdin.readline
n = int(input())

inf = int(1e9)
graph=[list(map(int, input().split())) for _ in range (n)]
distance = [[inf] * n for _ in range (n)]
def dijkstra(graph, n):
    q = [] # 우선순위 큐를 만들기 위해 빈 리스트 생성
    # 이동하기 위해 dx, dy 리스트 생성
    dx=[-1, 1, 0, 0]
    dy=[0, 0, -1, 1]
    # 그래프를 좌표로 구현 했기 때문에 튜플형태로 start를 받는다 
    heapq.heappush(q, (graph[0][0], 0, 0))
    distance[0][0] = graph[0][0]
    while q:
        cost, x, y = heapq.heappop(q)
        if cost > distance[x][y]:
            continue # 이미 갱신 되었으면 
        linked_point=[]
        for i in range (4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0<= nx < n )and (0 <= ny <n ):
                linked_point.append((graph[nx][ny], nx, ny))
        for i in linked_point:
            next_cost = cost + i[0]
            # 계산한 거리가 distance에 기록된 누적 거리보다 적다면
            if next_cost < distance[i[1]][i[2]]:
                distance[i[1]][i[2]] = next_cost    
                heapq.heappush(q, (next_cost, i[1],i[2]))
    return distance[n-1][n-1]
print(dijkstra(graph,n))