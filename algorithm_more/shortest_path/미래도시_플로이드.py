import sys
input= sys.stdin.readline
inf=int(1e9)
n , m =map(int,input().split())
graph=[[inf] * (n + 1) for _ in range (n+1)]

for i in range (m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int,input().split())

for i in range (n+1):
    graph[i][i] = 0

for a in range (n+1):
    for b in range (n+1):
        for c in range (n+1):
            if graph[b][a] + graph[a][c] < graph[b][c]:
                graph[b][c]= graph[b][a] + graph[a][c]

if graph[1][k] != inf and graph[k][x] != inf:
    print(graph[1][k]+graph[k][x])
else:
    print(-1)

print(graph)
