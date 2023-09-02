import sys
input= sys.stdin.readline()
n = int(input())
# 연산을 수행하고자 하는 리스트
data= list(map(int,input().split()))
# 각 연산자의 개수
add, sub, mul, div = map(int, input().split())

# 최솟값과 최댓값 초기화
min_value= 1e9
max_value= -1e9

# dfs 메서드로 i는 연산횟수 기록 1부터 시작하는이유는 n-1번의 개수를 실행 
def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    # 모든 연산자를 전부 사용한 경우 최솟값과 최댓값 업데이트
    if i ==n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else: # 아직 연산횟수가 남았을 경우 재귀적으로 계산을 수행한다
        # 연산기호를 사용할 때 마다 재귀적으로 수행한다
        # data의 i번째 행이 계산에 사용된다
        # 이것도 백트래킹의 과정이라고 볼 수 있다 모든 경우를 확인해야하므로 내 경우에서 덧셈을 한경우에서 dfs 시작 + 덧셈 안한경우에서도 시자갷야하므로
        # 다시 뺄셈을 해줘야한다  즉 변화한상태에서 재귀함수를 돌리고 다시 원상태로 되돌려놓는 것
        if add > 0:
            add -= 1
            dfs (i+1, now + data[i] ) 
            add += 1
        if sub > 0:
            sub -= 1
            dfs (i+1, now - data[i] ) 
            sub += 1
        if mul > 0:
            mul -= 1
            dfs (i+1, now * data[i] )
            mul += 1 
        if div > 0:
            div -= 1
            dfs( i+1, int(now/ data[i] ) )
            div += 1 

# dfs 호출
dfs(1, data[0])
print(max_value)
print(min_value)