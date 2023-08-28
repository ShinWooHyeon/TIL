N=int(input())
stu=[input().split() for _ in range(N)]

ans=sorted(stu,key=lambda x:x[1])
for i in range(len(ans)):
    print(ans[i][0],end=' ')