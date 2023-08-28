now=list(input())
board=['a','b','c','d','e','f','g','h']
for i in range(len(board)):
    if now[0]==board[i]:
        x= i+1
        break
y= int(now[1])
dx=[-2, -2, 2 , 2, -1, -1, 1, 1]
dy=[-1 , 1, -1, 1, -2, 2, -2, 2]
# steps=[(2,-1),(2,1)...] 이런식으로도 풀이 가능
cnt=0
for i in range(len(dx)):
    nx= x+dx[i]
    ny= y+dy[i]
    if nx <1 or nx>8 or ny<1 or ny>8:
        continue
    cnt+=1
print(cnt)