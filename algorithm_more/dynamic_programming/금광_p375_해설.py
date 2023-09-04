# 점화식 개념자체는 동일하나 해설 코드가 좀더 깔끔
T = int(input())
for _ in range (T):
    n , m = map(int, input().split())
    gold_graph = list(map(int, input().split()))
    graph=[gold_graph[m * i : m * (i + 1)] for i in range(n)]

    # 다이나믹 프로그래밍 진행
    for j in range(1, m):
        for i in range (n):
            # 왼쪽 위에서 오는 경우:
            if i == 0:
                left_up = 0 #그냥 0인경우 1가지니까 제외시켰네 이래서 좀더 깔끔하게 보인듯
            else:
                left_up = graph[i-1][j-1]
            
            if i == n-1:
                left_down = 0
            else:
                left_down = graph[i+1][j-1]
            
            left = graph [i][j-1]
            graph[i][j] = max(left_down, left, left_up) + graph[i][j]
    max_value=0
    for i in range (n):
        max_value=max(max_value,graph[i][m-1])
    print(max_value)