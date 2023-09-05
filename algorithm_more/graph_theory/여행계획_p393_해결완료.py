# 여행계획
def find_parent(parent, x):
    if parent[x] != x:
        parent[x]= find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 여행지의 수 n, 여행계획에 속한 도시의 수 m
n, m = map(int, input().split())
# 간선 정보 행렬일 경우 행렬을 인접 리스트로 바꾸고 풀이를 진행한다
graph_array =[list(map(int, input().split())) for _ in range (n)]
tour_list=list(map(int, input().split()))
edges= []
parent=[0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i
for i in range (n):
    for j in range (n):
        if graph_array[i][j] ==1:
            edges.append((i + 1, j + 1))

for edge in edges:
    a, b = edge
    union_parent(parent, a, b)
print(edges)
print(parent)