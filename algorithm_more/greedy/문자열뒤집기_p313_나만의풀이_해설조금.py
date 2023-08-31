# 문자열 뒤집기 # 백준에서는 틀렸다고 나오는데 왜 틀린지를 ㅁㄹ
s=list(input())
change=0
for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        change+=1
print((change+1)//2)

