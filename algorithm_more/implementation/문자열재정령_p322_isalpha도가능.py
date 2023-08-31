s=list(input())
ans=[]
num=0
for i in s :
    try:
        num+=int(i)
    except ValueError:
        ans.append(i)
ans.sort()

print(''.join(ans)+str(num))

# 해설과 동일하지만 try except 구문이 아닌 isalpha 함수로 알파벳 확인