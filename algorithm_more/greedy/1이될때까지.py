import sys
input=sys.stdin.readline
N, K= map(int,input().split())
m = 0
d = 0
while True:
    if N % K ==0:
        N //=K
        d += 1
    else:
        N -= 1
        m += 1
    if N ==1:
        print(m+d)
        break
