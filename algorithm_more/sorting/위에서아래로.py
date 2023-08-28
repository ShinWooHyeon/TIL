N=int(input())
nums=[int(input()) for _ in range(N)]
ans=sorted(nums,reverse=True)
for i in ans:
    print(i, end=' ')