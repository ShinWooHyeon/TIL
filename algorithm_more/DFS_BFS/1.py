from collections import deque
n , m =map(int,input().split())
maze=[list(map(int,input())) for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        x , y = queue.popleft()
        # 4가지 방향 
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            #미로찾기 
            if nx<=-1 or nx>=n or ny<=-1 or ny>=m:
                continue
            if maze[nx][ny]==0:
                continue
            #처음 방문이여야지 칸수 증가 , 즉 이미 숫자가 증가되어있는 상태라면? 방문한거니까 방문칸수를 어차피 증가시키지 않는다
            if maze[nx][ny]==1:
                maze[nx][ny]=maze[x][y]+1
                queue.append((nx,ny))
    return maze[n-1][m-1]
print(bfs(0,0))