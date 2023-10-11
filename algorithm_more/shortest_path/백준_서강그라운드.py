import sys
input = sys.stdin.readline
# n 노드의 개수, r 간선의 개수, m 수색범위
n, m, r = map(int, input().split())
inf = 1e9
# 노드별 아이템을 입력받는다
items=[0]
items.extend(list(map(int, input().split())))

graph =[[inf] * (n + 1)  for _ in range (n + 1)]

# 그래프 양방향이므로 양방향으로 입력받는다
for i in range (r):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

# 자기자신 가는 길은 0
for i in range (1, n + 1):
    graph[i][i] = 0

for k in range (1, n + 1):
    for i in range (1, n + 1):
        for j in range (1, n + 1):
            graph[i][j] = min (graph[i][j], graph[i][k]+graph[k][j])
result = 0
for i in range (1, n + 1):
    cnt = 0
    for j in range (1, n + 1):
        if graph[i][j] <= m:
            cnt += items[j]
    result = max(result, cnt)

print(result)