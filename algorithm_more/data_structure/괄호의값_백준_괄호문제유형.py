# 괄호길이 짝수면 0 출력
# 덱에서 앞에서 popleft한게 (, [ 둘중 하나여야 하며

blank = list(input())
stack= []
answer = 0
cal = 1
for i in range (len(blank)):
    if blank[i] == '(':
        stack.append('(')
        cal *= 2
    elif blank[i] == '[':
        stack.append('[')
        cal *= 3
    elif blank[i] == ')': # 스택이 비어있거나 바로앞이 '[인 경우가 문제, ]인 경우는 이미 고려되어서 없을 것임
        if not stack or stack[-1] =='[':
            answer = 0
            break
        if blank[i-1] == '(' :
            answer += cal
        stack.pop()
        cal//= 2             
    else: # 스택이 비어있거나 바로앞이 '[인 경우가 문제, ]인 경우는 이미 고려되어서 없을 것임
        if not stack or stack[-1] =='(':
            answer = 0
            break
        if blank[i-1] == '[' :
            answer += cal
        stack.pop()
        cal//= 3             
if stack:
    print(0)
else:
    print(answer)