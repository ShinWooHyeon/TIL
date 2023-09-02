# 감시피하기
import sys
from itertools import combinations
import copy
input = sys.stdin.readline
n= int(input())
graph=[]
t_point=[]
x_point =[]
for i in range (n):
    line= list(input().split())
    for j in range (n):
        if line[j] == 'T':
            t_point.append((i, j))
        elif line[j]=='S':
            x_point.append((i,j))
    graph.append(line)
candidate=list(combinations(x_point,3))
print(t_point)

def teacher_find(graph_built, t_point):
# 이 함수는 그래프가 바뀌어있다고 가정 선생들이 찾는 함수를 정의하고
# 새로운 함수에서 각 후보군에서 teacher_find 함수를 써야한다 
    for i in t_point:
        a, b = i
        for c in range(n-1-a):
            if graph_built[a+c][b]=='O':
                break
            if graph_built[a+c][b] == 'S':
                return False
        for c in range(a):
            if graph_built[a-c][b]=='O':
                break
            if graph_built[a-c][b] == 'S':
                return False
        for c in range(n-1-b):
            if graph_built[a][b+c]=='O':
                break
            if graph_built[a][b+c] == 'S':
                return False
        for c in range(b):
            if graph_built[a][b-c]=='O':
                break
            if graph_built[a][b-c] == 'S':
                return False
            
    return True     
# 후보마다 함수쓰고 4가지 중 1개라도 실패하면 return False 하
def check_teacher_find(graph, candidate, t_point):
    for x in candidate:
        graph_built=copy.deepcopy(graph)      
        for i in x:
            a, b = i
            graph_built[a][b] ='O'
        
        if teacher_find(graph_built,t_point) :
            return True
    return False

if check_teacher_find(graph, candidate, t_point):
    print('YES')
else:
    print('NO')
