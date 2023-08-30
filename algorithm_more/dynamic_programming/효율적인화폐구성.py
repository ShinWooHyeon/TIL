n , m = map(int,input().split())
mc = [int(input()) for _ in range(n)]
mc.sort()
d=[10001]*(m+1)
d[0]=0
for k in mc:
    for i in range(k,m+1):
        if d[i-k]!=10001:
            d[i]=min(d[i-k]+1,d[i])
print(d[:i+1])
if d[i]==10001:
    print(-1)
else:
    print(d[i])
