import sys
input = sys.stdin.readline

# 상, 하, 좌, 우
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# INPUT
N, M = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

max_value = 0
# dfs에 거리를 지속적으로 기록하기 위해 거리 변수 설정
# 자기 포함 4, 총 3번 이동까지 가능하기 때문에 이동횟수도 기록한다
def dfs(i, j, dsum, cnt):
    global max_value
    if cnt == 4 :
        max_value = max(dsum, max_value)
        return # 아무것도 없이 그냥 함수 종료시키기 위해서
    for i in range (4):
        nx = i + move[i][0]
        ny = j + move[i][1]
        if 0<= nx < N and 0 <= ny < N  and not visited[nx][ny]: # DFS 돌릴때 visited True하고 dfs하고 다시 false해서 브루트포스하는 개념잡기
            visited[nx][ny] = True
            dfs(nx, ny, dsum + board[nx][ny], cnt+1)
            visited[nx][ny] = False 
        

def exce(i,j) :
    global max_value
    for i in range (4):
        tmp = board[i][j]
        for k in range (3):
            t= k % 4
            nx = i + move[t][0]
            ny = i + move[t][1]

            if not  (0 <=nx < N and 0 <= ny < N):
                tmp = 0
                break
            tmp += board[nx][ny]
        #최댓값
        max_value = max(max_value, tmp) # tmp가 기록되다가 여기서 문제 생길 수 있기 때문에


for i in range (N):
    for j in range (N):
        visited[i][j] = True
        dfs(i, j, board[i][j], 1)
        visited[i][j] = False
    
        exce(i, j)

print(max_value)