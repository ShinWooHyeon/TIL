n , m = map(int,input().split())
ice=[]
for i in range(n):
    ice.append(list(map(int,input())))

# dfs를 정의해야 하는데 모든 노드를 방문하도록 정의한다
# 이 때 (0,0)에서 이미 dfs를 돌려보면 (0,1)등이 방문처리가 되기 때문에 후에 if ice[x][y]==0 조건이 되지 않아
# 연결된 모든 지점들을 시작점 한점에서만 dfs를 돌려보면 True값을 1개만 얻을 수 있다 
# 마지막 return False는 if 절 즉 구멍이 뚫려있는 부분의 경우에만 return을 하기 위해서 나머지의 경우 모두 false
def dfs(x,y):
    if x<= -1 or x>=n or y<=-1 or y>=m:
        return False
    if ice[x][y]==0:
        ice[x][y]=1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False
cnt=0
for j in range(n):
    for k in range(m):
        if dfs(j,k)==True:
            cnt+=1
print(cnt)

