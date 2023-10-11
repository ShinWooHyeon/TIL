# bfs 로 해결해야겠다
from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range (n)]
print(graph)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited=[[False]* m for _ in range (n)]

def bfs(graph, start):
    x, y = start
    visited[x][y]= True
    q=deque([(x, y)])
    while q:
        # graph에 거리 표시하고 있으니까
        x, y = q.popleft()
        for i in range (4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny]!=0:
                visited[nx][ny] = True
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
bfs(graph, (0,0))
print(graph[n-1][m-1])