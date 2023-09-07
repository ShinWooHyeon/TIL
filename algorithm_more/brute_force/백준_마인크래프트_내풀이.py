# N, M, B가 주어진다
# N이 i+2, 첫줄은 (0,0)  ~ (n-1,M-1)
# 인벤토리 블록개수 99
# 인벤토리 개수를 고려한다
import sys
import math
input = sys.stdin.readline
#높이를 일단 모두 같게 해야하는데 
# 블록개수 합 구하고 반올림 근데 만약 올림이라면 개수차이만큼 block이 인벤토리에 있으면 가능
# 없으면 목표 높이 2개를 가지고 평균 높이 올림, 반올림한거 비교를 하는데 
# 시간, height를 정렬하고 0번 인덱스 출력하면 된다
n, m, b = map(int, input().split())
block_world=[]
sum_h = 0
for i in range (n):
    line = list(map(int, input().split()))
    block_world.append(line)
    sum_h += sum(line) 
height1 = int(sum_h/ (n *m))
height2 = height1 + 1
result= []

if height2 * n * m > (b + sum_h):
    case = [height1]
else:
    case = [height1, height2]
for height in case:
    case_time= 0
    for i in range (n):
        for j in range (m):
            dist = block_world[i][j]- height
            if dist > 0 :
                case_time += 2* dist
            else:
                case_time -=  dist
    result.append((case_time, height))
result.sort()
a, b = result[0]
print(a, b)