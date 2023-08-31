# 볼링공 고르기 
n , m = map(int, input().split())
ball_list= list(map(int,input().split()))
set_ball=list(set(ball_list))
# 아직까지는 시간복잡도 o(n) 반복도 아니니까
# 겹치는 무게 기록
same_ball=0
for i in set_ball : # 최대 m개
    x = ball_list.count(i)
    if x !=1:  # 카운트 함수쓰면 최대 n개  시간복잡도는 O(MN)
        same_ball+= int(x*(x-1)/2)

print(int(n*(n-1)/2)-same_ball)