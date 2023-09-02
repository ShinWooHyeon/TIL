from itertools import combinations
import sys
import copy
# 내 풀이도 나쁜게 아닌거 같은데 한번 복습할때 봐보자 
input = sys.stdin.readline
n, m = map(int, input().split())
virus_map = []
blank=[]

virus_cnt=0
for i in range (n):
    virus_map.append(list(map(int, input().split())))
    for j in range (m):
        if virus_map[i][j]==0:
            blank.append((i,j))
        if virus_map[i][j]==2:
            virus_cnt+=1
blank_cnt=len(blank)
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]

candidate = list(combinations(blank, 3))

def dfs(virus_map, n, m):
    change=0
    for x in range (n):
        for y in range (m):
            if virus_map[x][y] !=2:
                continue
            else:
                for i in range (4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx >=0 and nx <n and ny >=0 and ny<m and virus_map[nx][ny] == 0:
                        virus_map[nx][ny] = 2
                        change+=1
    return change            

result=[]
for a in candidate :
    c_virus_map = copy.deepcopy(virus_map)

    for b in a:
        x, y = b
        c_virus_map[x][y] = 1 # 여기서 3개가 변했을 것이고
    result.append(dfs(c_virus_map, n, m))

save = blank_cnt - (3 + min(result))  # 원래 safety존에서 3개는 벽을 세웠고 바뀐 개수만큼 더 안전공간이 줄었으므로 
print(min(result))
print(save)  