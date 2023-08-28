import sys
input=sys.stdin.readline
n, m=map(int,input().split())
x, y, direction =map(int,input().split())
# 방문위치 표시하기 위한 맵 생성
d=[[0]* m for _ in range (n)]
d[x][y]=1

game_map=[]
for i in range (n):
    game_map.append(list(map(int,input().split())))

dx=[-1, 0, 1,0]
dy=[0, 1, 0,-1]

def turnleft():
    global direction
    if direction>0:
        direction-=1
    else:
        direction=+3
cnt=1
# 네 방향을 모두 확인해야 하므로 turn을 체크하는 변수도 고려해야한다 
turn_cnt=0
while True:
    turnleft()
    nx= x+dx[direction]
    ny= y+dy[direction]
    if d[nx][ny] ==0 and game_map[nx][ny]!=1 :
        x=nx
        y=ny
        d[x][y]=1
        cnt+=1
        turn_cnt=0
        # 여기서 turn time을 더할 경우 회전 1번하고 직진하는데 계속 turn time이  쌓이는 문제가 발생한다
        # 또한 1단계로 초기화를 해야하기 때문에 4방향 모두 확인은 움직였을 때 다시 초기화 시켜야 하낟 
        continue
    else:
        turn_cnt+=1
    if turn_cnt==4:
        nx=x-dx[direction]
        ny=y-dy[direction]
        if game_map[nx][ny]==0:
            x=nx
            y=ny
        else:
            break
        turn_cnt=0
        # 이 문제의 포인트는 1단계로 돌아가기 위해서는 turn_cnt를 계속 초기화 시켜야 한다는 것!
        # 실제로는 외곽도 바다라는 점을 고려해야 한다 ! 
print(cnt)