# 편집거리
# 2차원 테이블을 통해 문제를 해결한다. 
# 행과 열에 해당하는 문자가 서로 같다면, 왼쪽위에 해당하는 수를 그대로 대입한다 
# dp[i][j]는 a의 index i까지의  문자가 b에서 index j 까지의 문자와 같기 위해서 필요한 최소 횟수
# 2차원 리스트를 만든다라고 생각한다 ()
def edit_dist(str1, str2) :
    n = len(str1)
    m = len(str2)
    dp = [[0] * (m+1) for _ in range(n+1) ]
    # dp 초기값 1열은 문자 n으로 1행은 문자 j로 
    for i in range (1, n + 1):
        dp[i][0] = i  # str1이 아무것도 없는 문자가 되기 위해서는 자기 길이만큼의 횟수가 필요하니까
    for j in range (1, m + 1):
        dp[0][j] = j
    
    for i in range (1, n + 1):
        for j in range(1, m + 1):
            # str은 길이가 그대로기 때문에 n+1, m+1 기준에서는 -1 해줘야 한다 
            if str1[i-1] == str2[j-1]: # 실제 dp에서는 i번째 까지가 j번째 까지랑 같을때
                dp[i][j] = dp[i-1][j-1]
            else:
                # dp[i][j] 직전을 고려해서 1번 바뀌어서 될 수 있는 경우의수 들중 가장 작은 값 + 바꾼 횟수 1회가 dp값이 된다 
                # 행의 값이 1작은 값은 바꾸고싶은 문자가 1개 적은거니까 1개 삽입해야 하고 , 즉 
                # 열의 값이 1작은 값은 바뀐문자가 1개 더 긴 상황이니까 1개 삭제해야 하고  
                # 행, 열 둘다 작은 값은 i-1, j-1 까지 같고 i번째 문자를 j 번째 문자로 교체하 ㄴ경우이다
                dp[i][j] = 1+ min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

    return dp[n][m]   
    # 우리의 목표는 a의 n까지의 길이가 b의 m까지의 길이고 가는 것이므로 dp[n][m] 을 구해야 한다

str1 = input()
str2 = input()
print(edit_dist(str1, str2))