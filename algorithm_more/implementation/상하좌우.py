import sys
N = int(input())
x, y = 1 , 1
dx=[0, 0 , -1 ,1]
dy=[-1, 1, 0 , 0]
direction=['L','R','U','D']
orders=input().split()
for order in orders:
    for i in range(len(direction)):
        if order== direction[i]:
            nx= x + dx[i]
            ny= y + dy[i]
        
    if nx<1 or nx>5 or ny<1 or ny>5 :
        continue
    x , y = nx,ny
print(x,y)