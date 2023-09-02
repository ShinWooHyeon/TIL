# 문자열 뒤집기 # 제대로 해결
s=list(input())
change=0
for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        change+=1
print((change+1)//2)


# 해설의 경우 0을 뒤집는 경우와 1을 뒤집는 경우를 비교해서 풀이 