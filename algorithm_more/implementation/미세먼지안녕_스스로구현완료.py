#  미세먼지 확산 (중요한건 미세먼지 확산이 동시에 일어나야 하므로)
# 변화를 기록하는 크기가 똑같은 그래프도 필요하다
# 2중 for문을 돌며 변화량을 전부 기록한다
#  정화전에 변화량을 고려한 그래프로 바꾼다
import sys
import copy
input = sys.stdin.readline
r, c, t = map(int, input().split())
cleaner =[]
room = []
# 방을 입력받고 이때 공기청정기의 위치도 기록한다
for i in range (r):
    line = list(map(int, input().split()))
    room.append(line)
    if line[0] == -1:
        cleaner.append(i)

def right_move(room, a):
    for i in range (2, c):
        clean_change[a][i]= room[a][i-1]

def up_move(room, a):
    if a != r-1:
        for i in range (a-1, -1, -1):
            clean_change[i][c-1] = room[i+1][c-1]
    else:
        while True:
            if room[a-1][0] != -1 :
                clean_change[a-1][0] = room[a][0]
                a -=1
            else:
                break
def left_move(room, a):
    for i in range (c-2, -1, -1):
        clean_change[a][i] = room[a][i + 1]
def down_move(room, a):
    if a != 0 :
        for i in range (a+1, r):
            clean_change[i][c-1] = room[i - 1][c-1]
    else:
        while True:
            if room[a + 1][0] != -1 :
                clean_change[a + 1][0] = room[a][0]
                a +=1
            else:
                break  
dx = [1, -1, 0, 0]
dy = [0, 0 , 1, -1]
for d in range (t):
    # 2중 for문을 돌며 변화량을 기록해야 한다 변화량 기록할 그래프도 필요
    room_change =[[0]* c for _ in range (r)]
    for i in range (r):
        for j in range (c):
            if room[i][j]!=0 and room[i][j]!= -1:
                out_air = room[i][j] // 5
                for k in range (4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0<= nx < r and 0 <= ny <c and room[nx][ny] != -1:
                        room_change[nx][ny] += out_air
                        room_change[i][j] -= out_air
    for i in range(r):
        for j in range(c):
            room[i][j] += room_change[i][j]
    #바뀐 룸에서 공기청정기를 가동한다 
    # 공기청정기가 있는 두행이 한칸씩 이동하고 
    # 공기청정기로 빠뀐 변화를 기록할 그래프 생성
    clean_change = copy.deepcopy(room)
    for i in range(2):
        clean_change[cleaner[i]][1] = 0
        if i == 0:
            right_move(room, cleaner[i])
            up_move(room, cleaner[i])
            left_move(room, 0)
            down_move(room, 0)
        else:
            right_move(room, cleaner[i])
            down_move(room, cleaner[i])
            left_move(room, r-1)
            up_move(room, r-1)
    room = clean_change
answer = 0
for i in range (r):
    for j in range (c):
        answer += room[i][j]
print(answer+2)