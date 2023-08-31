n = int(input())
k = int(input())
graph=[[0]* (n+1)  for _ in range(n+1)]
for _ in range (k):
    a, b = map(int,input().split())
    graph[a][b]=1

order=[]
l = int(input())
for _ in range (l):
    e, f =input().split()   
    order.append((int(e), f))
# 현재 위치를 기록할 필요가 있다 
dx=[0, 1, 0 , -1]
dy=[1, 0, -1,  0]

# 방향이 4번이상 바뀌면 -5 이상이 될 수 있으므로 4로 나눈 나머지여야한다 
def turn(direction, c) :
    if c == "L":
        direction=(direction-1) %4
    else:
        direction=(direction+1) %4  
    return direction

# 구현은 대부분 함수를 많이 만든다 함수 만드는 연습 !!
def simulate () :
    x, y = 1 , 1
# 여기서도 팁인데 새로운 뱀이 존재하는 행렬을 만드는게 아니라 숫자를 다르게 해서 같은 행렬에 표시해서 공간을 절약한다!!
    graph[x][y]= 2 #뱀의 머리가존재하는 위치를 2로 표시함
    direction = 0 #초기 방향은 동쪽
    time = 0 # 처음 시간도 0
    index = 0 #회전 정보 
    q = [(x,y)] # 뱀이 존재하고 있는 위치 꼬리정보 , 꼬리가 앞쪽이다 
    while True:
        nx = x+ dx[direction]
        ny = y+ dy[direction]
        # 맵 범위 안이며 뱀의 몸통이 없는 위치라면 
        if  1<= nx and nx <=n and 1<= ny and ny <= n and graph[nx][ny]!=2:
            #사과가 없다면 이동후 꼬리 제거
            if graph[nx][ny] ==0:
                graph[nx][ny] =2
                q.append((nx,ny)) #새로운 머리 좌표 삽입하고 
                px, py = q.pop(0) # 뱀 위치 정보에서 빼고 아마 2로 기록되있으니 이것도 지워줘야하므로
                graph[px][py] = 0 # 0으로 수정해준다
            # 사과가 있따면 , else 쓰면 안되는 이유 2일수도 있으니까 근데 2일 수가 없는데
            if graph[nx][ny] == 1:
                graph[nx][ny]=2
                q.append((nx,ny))
        # 벽이나 몸과 부딪혔다면 종료해야지
        else:
            #이동후 부딪히므로 time 올려주고 break
            time+=1
            break
        x , y = nx, ny  #머리는 무조건 이동하므로 다음 위치로 이동하고
        time +=1
        # 아직 회전 할 수 있으면 이게 1인게 말이 안되지
        if index < l and time == order[index][0]:
            direction=turn(direction, order[index][1]) 
            index+=1
    return time

print(simulate())