#프로그래머스
#https://school.programmers.co.kr/questions/55001 반례 이유
def find_parent(parent, x):
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

def solution(n, computers):
    parent= [0] * (n )
    for i in range (n):
        parent[i] = i
    # 연결된 간선들을 튜플로 받아 리스트에 넣고 집합으로 간단하게 한다 
    # 그냥 i < j보다 작다는 조건주고 union하면 될거같다 
    for i in range(n):
        for j in range (n):
            if computers[i][j] ==1 and  i != j:
                union_parent(parent, i , j )
    for i in range (n):
        find_parent(parent, i)
    answer = len(set(parent))
    return answer