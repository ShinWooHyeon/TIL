# 정확하 순위
n , m = map(int, input().split())
cal_check_in=[0] *(n+1)
cal_check_out =[0] * (n+1)
inf= int(1e9)
graph = [[inf] * (n+1) for _ in range (n+1)]

for _ in range (m) :
    a, b = map(int,input().split())
    graph[a][b] = 1

for k in range (1, n+1):
    for a in range (1, n+1):
        for b in range (1, n+1):
            graph[a][b] = min( graph[a][b], graph[a][k] + graph[k][b])

for i in range (1, n+1):
    for j in range (1, n+1):
        if graph[i][j] != inf:
            cal_check_out[i] += 1
            cal_check_in[j] += 1
cnt =0
for i in range (1, n+1):
    if cal_check_in[i] + cal_check_out[i] == n-1:
        cnt+=1
print(cnt)