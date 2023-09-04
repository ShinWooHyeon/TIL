# 3가지 방향 

def gold_find(graph, n, m):
    dx = [-1, 0, 1]
    dy = [-1, -1, -1]
    find_graph= [[0] * m for _ in range(n)]
    find_graph[0]= graph[0]
    final_gold = -1
    for j in range (1, m ):
        for i in range (n):
            gold_cand= -1
        
            for k in range (3):
                nx = i + dx[k]
                ny = j + dy[k]
                if  0 <= nx < n :
                    if gold_cand < graph[nx][ny]:
                        gold_cand = graph[nx][ny]
            find_graph[i][j] = gold_cand + graph[i][j]         
            if j == m-1:
                if find_graph[i][j] > final_gold:
                    final_gold = find_graph[i][j]
    return final_gold

T = int(input())
for _ in range (T):
    n , m = map(int, input().split())
    gold_graph = list(map(int, input().split()))
    graph=[gold_graph[m * i : m * (i + 1)] for i in range(n)]
    dx = [-1, 0, 1]
    dy = [-1, -1, -1]
    find_graph= [[0] * m for _ in range(n)]
    for x in range(n) :
        find_graph[x][0] = graph[x][0]
    print(find_graph)
    final_gold = -1
    for j in range (1, m ):
        for i in range (n):
            gold_cand= -1
            for k in range (3):
                nx = i + dx[k]
                ny = j + dy[k]
                if  0 <= nx < n :
                    if gold_cand < find_graph[nx][ny]:
                        gold_cand = find_graph[nx][ny]
            find_graph[i][j] = gold_cand + graph[i][j]         
            if j == m-1:
                if find_graph[i][j] > final_gold:
                    final_gold = find_graph[i][j] 
    print(final_gold)
# 다음열의 숫자들은 바로 앞 열  