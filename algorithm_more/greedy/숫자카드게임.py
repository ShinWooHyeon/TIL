import sys
input=sys.stdin.readline

n , m =map(int,input().split())

big_num=0
for i in range(n):
    cards=sorted(list(map(int,input().split())))
    if cards[0]>big_num:
        big_num = cards[0]

print(big_num)    
