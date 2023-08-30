#개미창고 (내 아이디어도 거의 맞았는데 아쉽다!!!)
n = int(input())
box = list(map(int,input().split()))
d=[0] * 101
d[0]=box[0]
d[1]=max(box[0],box[1])

for i in range(2,n):
    d[i]=max(d[i-1],d[i-2]+box[i])

print(d[n-1])