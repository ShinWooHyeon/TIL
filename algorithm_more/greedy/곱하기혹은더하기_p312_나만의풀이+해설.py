# 0이 아닌경우는 무조건 곱셈이 더 크다  (1을 고려 못함 틀렸음 )
s=list(map(int,input()))
if s[0]!=0:
    max_num=s[0]
    for i in range(len(s) - 1):
        if s[i+1]!=0:
            max_num *= s[i+1]
else:
    for i in range(len(s) - 1):
        if s[i+1]!=0:
            max_num=s[i+1]
            break
    for j in range(i+1,len(s)-1):
        if s[i+1]!=0:
            max_num *= s[j+1]

print(max_num)
# 해설
# 그냥 결과값과 다음 수를 비교해서 0또는 1이 있으면 무조건 더하고 그게 아니라면 곱한다 !!!
s=list(map(int,input()))
result=s[0]
for i in range(1,len(s)):
    if result > 1 and s[i] >1:
        result *= s[i]
    else:
        result += s[i]

print(result)
