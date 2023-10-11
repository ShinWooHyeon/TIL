# 각 방향으로 이동하는 함수를 만들어야 한다 
# 아마 시뮬레이션을 돌리며 min 횟수를 갱신하는 방식으로 접근해야한다 
# 이동할 때 주의점 두 구슬이 같은 지점에 있을 수 없다  => 움직였을 떄 두 지점이 같으면 이동한 거리 계산, 
# 그 거리가 짧은 구슬이 같은 지점의 위치가 되고 
# 둘 다 빠지면 안된다 
from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

# 그래프를 입력받는다 , 이때 빨간 공과 파란공의 시작 포인트를 알아야 한다 
graph =[]
for i in range (n):
    line = list(input())
    for j in range (len(line)):
        if line[j] == 'R':
            rx, ry = i, j
        if line[j] == 'B':
            bx, by = i, j

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 이 문제에 bfs 개념이 왜 쓰였는지를 잘 생각해보자 여러번 돌려서 자기 위치에 왔을때 이미 한번 왔으면 그때랑 똑같기 때문에 고려할 필요가 없다
# bfs 시작부분에서 count를 지정하고 간다 

def bfs (rx, ry, bx, by):
    q = deque()
    q.append((rx, ry, bx, by))
    visited =[]
    visited.append((rx, ry, bx, by))
    count = 0
    while q:
        # 백준 경쟁적 전염 문제 처럼 큐의 길이로 하면 사이클대로 bfs를 하고 count를 확인할 수 있다
        for _ in range (len(q)):
            # popleft해서 나오는 애들은 
            rx, ry, bx, by = q.popleft()
            # 움직이고 바로 결과를 확인하는게 아니라 그 다음 while 문에서 pop하고 상태를 확인, 즉 이때도 count가 10이면 문제 없이 출력 가능 
            if count >10:
                print(0)
                return
            if graph[rx][ry] == 'O' :
                print(1)
                return 
            for i in range (4):
                # 이 방식을 잘 생각해보자 자기 앞이 #이거나 구멍일 때 까지 움직일 것이다
                # nrx에 지속적으로 더하려면 += 써야되고 그러면 nrx 미리 지정되있어야한다
                # 여기선 원래 index 범위 고려해야하는데 가장자리 모두 # 이기 때문에 고려 x
                nrx ,nry = rx, ry
                while True:
                    nrx += dx[i]
                    nry += dy[i]
                    if graph[nrx][nry] =='#':
                        nrx -= dx[i]
                        nry -= dy[i]
                        break
                    if graph[nrx][nry] =='O':
                        break
                
                nbx, nby = bx, by
                while True:
                    nbx += dx[i]
                    nby += dy[i]
                    if graph[nbx][nby] =='#':
                        nbx -= dx[i]
                        nby -= dy[i]
                        break
                    if graph[nbx][nby] =='O':
                        break
                # b가 먼저 들어가거나 동시에 들어가도 안된다 즉 b는 굴렸을 때 들어가면 안된다
                if graph[nbx][nby] == 'O':
                    continue #실패했으니 이 과정 생략하고 큐를 돌려야한다
                # 둘이 같은 곳에 있어선 안된다 
                if nrx == nbx and nry == nby :
                    # 거리를 비교해서 
                    if abs(nrx-rx) +abs (nry- ry) > abs(nbx -bx) + abs(nby - by) :
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i] 
                # 다 돌고 나서 nrx, nry ,nbx, nby가 다 결정 되었을때 visited를 확인하고 
                if (nrx, nry, nbx, nby) not in visited:
                    visited.append((nrx, nry, nbx, nby))
                    q. append((nrx, nry, nbx, nby))
        count += 1