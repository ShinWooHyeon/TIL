# 1번부터 N번까지
from collections import deque
N, K = map(int, input().split())
start = [i for i in range (1, N + 1)]
q = deque(start)
answer=[]
while q:
    for i in range (1, K+1):
         a = q.popleft()
         if i == K: 
            answer.append(a)
            break
         q.append(a)
         
print('<', end='')
for i in range (len(answer)-1):
    print(answer[i], end='')
    print(',', end=' ')
print(answer[-1],end='')
print('>')