# 백준 아기상어
# N x N 크기 물고기 M마리 아기상어 1마리
# 아기상어 크기 2 초에 이동
# 자신보다 큰 물고기 있는칸은 지나갈수 없다
# 나머지 칸 모두 지나갈 수있다
# 작은 물고기만 먹을 수 있고 같은 물고기는 못 먹어도 지나갈 수 있다다
# 더이상 먹을 물고기 없으면 엄마상어에게 도움요청
# 먹을 수 있는 물고기 1마리면 개 먹으러감
# 먹을수 있는 물고기 1마리보다 많으면 가장 가까운 물고기 먹으러감
# 거리는 지나야 하는 칸 개수의 최솟값
# 거리가 가까운 물고기가 많다면 가장 위에 물고기, 그런 물고기가
# 여러마리면 가장 왼쪽 물고기를 먹는다
# 이동은 1초 ,먹는건 바로 자긴과 크기가 같은수의 물고기를 먹을때마다 크기가 1증가함    
# 자신의 물고기 크기를 계속 기록해야하 
# 1번 일단 먹을 수 있는 물고기가 있는지 체크 
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
sea = []
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
for i in range (N):
    line = list(map(int, input().split()))
    sea.append(line)
    for j in range (N):
        if line[j] == 9:
            baby_fish= (i, j)
# 가장 가까운 먹이를 찾는 탐색 문제 BFS를 고려할 수 있다
# 후보리스트중 가장 가까운 것을 가야하므로 후보리스트를 반환해야 하는 것이 포인트 
time =0 
def bfs (x, y):
    visited = [[0] * N for _ in range (N)]
    queue=deque([(x,y)])
    cand= [] # 반환할 후보를 넣을 리스트
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range (4):
            nx = x + dx[i]
            ny = y + dy[i]
        # 여기가 포인트 전체 sea를 돌아다니며 후보군을 전부 찾을 것인데 거리를 표현하기 위해서 visited 사용하는거 보자
        # 또한 cand에는 작다는 조건만 충족하면 넣도록 한다
        # bfs를 한다는 것 자체가 현재 x, y가 아기상어의 위치이자 그때의 값이 아기상어의 값이므로
        # not visited여야지 방문한다가 bfs의 핵심 절대 까먹지 말자
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] ==0:
        #위에서 고려해도 되고 아래에서 크기 비교조건을 고려하면 어차피 다 고려된다.
        # 여기서 포인트 또 거리순으로 정렬할 것이기 때문에 거리를 고려해야한다
        # 처음은 0초인데 visited 때매 1로 시작했으므로 cand에 넣을때는 -1한값을 넣어준다
            if sea[x][y] > sea[nx][ny]  and  sea[nx][ny] !=0:
                visited[nx][ny] = visited[x][y] +1
                cand.append((visited[nx][ny] -1, nx, ny))
            # 아직 이동의 가능성 남아있으므로 q에 삽입해야함
            elif sea[x][y] == sea[nx][ny] :
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
            elif sea[nx][ny] ==0:
                visited[nx][ny] = visited[x][y] +1
                queue.append((nx, ny))
    # 후보리스트를 거리순으로 정렬하고 거리가 같다면 x기준 그다음이 y기준이다
    return sorted(cand, key = lambda x: (x[0], x[1], x[2]))
bx, by = baby_fish
size = 2
eat = 0
# 맨앞의 후보를 먹고 위치 이동후 다시 bfs
while True:
    sea[bx][by] = size # 자기 위치에 크기를 할당한다 
    cand = deque(bfs(bx, by))  
    # cand는 현재 후보군
    if not cand : #후보군이 없다면
        break
    # 가장 앞 후보리스트를 먹는다 (어차피 후보는 while문 돌면서 새로 생성되니까)
    using_time, x, y = cand.popleft()
    time += using_time
    eat += 1

    # 몇개 먹었고 몇고 이동했는지 체크한다 
    if size == eat:
        size += 1
        eat = 0
    sea[bx][by] = 0 # 현재 좌표를 0값으로 해야지 맨처음 출발하는 곳의 sea값이 0으로 바뀔 수 있음 
    bx, by = x, y # 다음 while문의 좌표를 후보군의 좌표로 바꿔준다  

print(time)