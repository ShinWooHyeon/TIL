from collections import deque
n, m, v = map(int, input().split())
# dfs는 자기 자신에서 시작해서 
visited1 = [False] * (n + 1)
visited2 = [False] * (n + 1)
graph = [[False] * (n + 1) for _ in range (n+1)]
for i in range (m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True
def dfs (start):
    visited1[start]= True
    print(start, end=' ')
    # 작은 번호부터 가기 위해 여기서는 for문을 돌린다 
    for i in range (1, n + 1) :
        if not visited1[i] and graph[start][i]:
              dfs(i)

def bfs (start):
    visited2[start] = True
    q= deque([])
    q.append(start)
    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in range (1, n + 1):
            if not visited2[i] and graph[now][i]:
                visited2[i] = True
                q.append(i)
dfs(v)
print()
visited= [False] * (n+1)
bfs(v)