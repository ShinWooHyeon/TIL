import sys
input = sys.stdin.readline
# 노드의 개수 n, 간선의 개수 m
# 크루스칼 알고리즘을 떠올리자
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
m = int(input())
parent= [0] * (n + 1)
for i in range (1, n + 1):
    parent[i] = i

# 간선을 담을 리스트 생성
nodes = []
for i in range (m):
    a, b, c = map(int, input().split())
    nodes.append((c, a, b))

nodes.sort()
# 거리 기록할 변수 저장
result = 0

# 그다음은 그냥 for문인데 
for node in nodes:
    cost, a, b = node
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)