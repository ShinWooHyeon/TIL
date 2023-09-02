# 치킨배달
import copy
from itertools import combinations
n , m = map(int, input().split())

graph= [list(map(int, input().split())) for _ in range (n)]
# 집 좌표와 치킨좌표들을을 정리한다 
home_place=[]
chicken_place=[]

for i in range(n):
    for j in range (n):
        if graph[i][j] == 2:
            chicken_place.append((i,j))
        if graph[i][j] == 1:
            home_place.append((i,j))
chicken_now = len(chicken_place)
# M개의 치킨집을 운영한다 => 현재 치킨집-M 개가 닫아야한다,

chicken_close = list(combinations(chicken_place, chicken_now - m))

# for문을 통해 치킨집 닫는 경우에 따라서 최소 도시

chicken_length = int(1e9)
for i in chicken_close:
    graph_changed = copy.deepcopy(graph)
    # 선택한 치킨집들이 닫는 경우 
    total_length=0
    for j in i:
        x, y = j
        graph_changed[x][y]=0
    print(graph_changed)
    # 바뀐 그래프에서 치킨집들의 치킨 거리를 구해야 한다 
    print(home_place)
    for k in home_place:
        nx, ny = k
        print(nx, ny, '집 좌표')
        breaker=False
        for a in range(1, n):
            for b in range (a+1):
                mx , my= b, a-b 
                if  ((nx + mx) >=0 and (nx +mx) <n ) and ((nx - mx) >=0 and (nx - mx) <n ) and\
                    ((ny + my) >=0 and (ny +my) <n ) and ((ny - my) >=0 and (ny -my) <n ) :
                    if graph_changed[nx + mx][ny + my] == 2 or  graph_changed[nx + mx][ny - my] == 2 or\
                        graph_changed[nx - mx][ ny + my] == 2 or  graph_changed[nx - mx][ny - my] == 2 :
                        print (nx, ny)
                        print( mx, my ,'집좌표에서 치킨발견')
                        total_length += a
                        print(total_length)
                        breaker=True
                        break
            if breaker ==True:
                break
    if chicken_length > total_length:
        chicken_length = total_length          
# 치킨거리를 구하는 함수를 구하고
# 조합하는 경우에서 최소 거리를 갱신하면서 구한다 


print(chicken_length)

