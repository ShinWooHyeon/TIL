# n 번째 큰수 
import heapq
n= int(input())
graph =[list(map(int, input().split())) for _ in range (n)]
q= []
for i in range(n):
    heapq.heappush(q,(-1 * graph[n-1][i], n-1, i))
# 힙에 맨 아랫줄 n개를 넣는다
# 만약 자신이 빠졌다면 자기 바로위를 큐에 삽입한다 
for i in range (n):
    a= heapq.heappop(q)
    if i == n-1:
        print(-1 * a[0])
    nx = a[1] -1
    ny = a[2] 
    heapq.heappush(q, (-1 * graph[nx][ny], nx, ny))

