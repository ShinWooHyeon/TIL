# 볼링공 고르기 # 내 풀이는 별로 좋지 않은 풀이 같다 해설이 중여 
n , m = map(int, input().split())
ball_list= list(map(int,input().split()))
set_ball=list(set(ball_list))
# 아직까지는 시간복잡도 o(n) 반복도 아니니까
# 겹치는 무게 기록
# 근데 이렇게 쓰면 for문마다 count 써야하니까 매우 비효율적이구나!!
# 해설처럼 count할 필요가 있다
same_ball=0
for i in set_ball : # 최대 m개 
    x = ball_list.count(i)
    if x !=1:  # 카운트 함수쓰면 최대 n개  시간복잡도는 O(MN)
        same_ball+= int(x*(x-1)/2)

print(int(n*(n-1)/2)-same_ball)

#--------------------------------------------------------------------
# 해설풀이
n , m = map(int, input().split())
ball_list= list(map(int,input().split()))

# 볼 개수 세는 리스트 생성
ball_cnt = [0] * 11

# 개수를 다 세고
for i in ball_list:
    ball_cnt[i]+=1

result = 0

for i in range (1, m+1):
    # n에서 i의 개수를 빼주는 이유는 2개를 고를때 이미 i를 고르는 모든 경우를 고려했기 때문이다  
    n-=ball_cnt[i]
    
    # i를 고르는 개수가 ball_cnt[i] 나머지를 고르는 개수가 n개 일 것이다
    result+= ball_cnt[i] * n

print(result)