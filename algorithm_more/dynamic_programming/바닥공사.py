# 바닥공사 
n = int(input())
d=[0]*1001
d[1]=1
d[2]=3
# 3가지 경우를 고려하면 안되는 이유는 이미 i-1 번째 덮개를 덮을때 고려가 되어있기 때문이다 
for i in range(3,n+1):
    d[i]=(d[i-1]+2*d[i-2]) %796796

print(d[n])