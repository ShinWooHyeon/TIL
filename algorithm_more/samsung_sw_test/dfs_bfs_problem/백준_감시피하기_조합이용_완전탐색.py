from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline
N =int(input())
road =[] 
student = []
teachers = []
space = []

# 선생님 포지션에서 학생들을 찾는 함수를 만든다

# 학생과 선생의 리스트를 만든다
for i in range (N):
    way = input().split()
    road.append(way)
    for j in range(len(way)):
        if way[j] == 'T':
            teachers.append((i, j))
        if way[j] == 'X':
            space.append((i, j))

def stu_find(teahers, N, road, cand):
    for teacher in teachers:
        # 왼쪽  탐색
        tx = teacher[1]
        ty = teacher[0]
        # 왼쪽방향
        for i in range (tx):
            if road[ty][tx-i] == 'S':
                return True
            if (ty, tx-i) in cand:
                break
        # 오른쪽
        for i in range (N - tx - 1):
            if road[ty][tx + i] == 'S':
                return True
            if (ty, tx + i) in cand:
                break
        # 위방향
        for i in range (ty):
            if road[ty - i][tx] == 'S':
                return True
            if (ty, tx-i) in cand:
                break
        # 아래방향 
        for i in range (N - ty - 1):
            if road[ty + i][tx] == 'S':
                return True
            if (ty + i , tx) in cand:
                break
    return False




# 후보들 조합이용해서 리스트 만들고
cands = list(combinations(space, 3))


# 각 후보들에 대해서
for cand in cands:
    # 각 cand에 대해서 False가 한 개라도 있으면 그 즉시 for문을 종료하고 끝낸다
    if not stu_find(teachers, N, road, cand) :
        print('YES')
        break
else:
    print('NO')