import sys
from collections import deque
input = sys.stdin.readline

# 시간을 기록해야 하고 , 방향도 기록해야 한다 %로 접근해야한다

# 뱀이 현재 어디에 위치하고 있는지 기록해야 하는데 이를 deque로 기록하고 append와 popleft를 사용하여 구현한다
n = int(input())
k = int(input())

# 사과 정보를 입력받는다
apple =[]
for _ in range (k):
    a, b = map(int, input().split())
    apple.append((a-1, b-1)) 

# 방향 변환 정보를 입력받는다
l = int(input())
directs ={}
for _ in range (l):
    a, b = input().split()
    directs[int(a)] = b

snake = deque()
snake.append((0,0))

hx, hy= 0, 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1 ,0]  
direction = 0
time = 0
while True:
    time += 1 # 이 문제에서는 이동 후 문제가 발생

    hx += dx[direction]
    hy += dy[direction]
    # 벽에 부딪힐 경우 멈추고
    if not ((0 <= hx < n) and (0 <= hy < n)):
        print(time)
        break
    # 다음 이동 좌표가 snake에 이미 있을 경우도 멈춰야 한다 
    if (hx, hy) in snake :
        print (time)
        break
    if (hx, hy) in apple :
        snake.append((hx, hy))
        apple.remove((hx, hy))
    else:
        snake.append((hx, hy))
        snake.popleft()

    # 벽에 부딪히지도 않고 자신과 만나지도 않는다면 시간을 보고 방향전환을 확인한다 
    # 시간이 끝난후 방향전환을 하므로 
    if time in directs.keys():
        change = directs[time]
        if change == 'L':
            direction = (direction -1) % 4
        else:
            direction = (direction +1) % 4
        