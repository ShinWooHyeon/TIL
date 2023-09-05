# 어두운 길 
# N개의 집, M개의 도로 각 집 0 ~ N-1
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b=  find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
nodes=[]
total=0
result=0
for i in range (m):
    a, b, c = map(int, input().split())
    nodes.append((c, a, b))
    total += c
nodes.sort()
parent=[0] * n
for i in range (n):
    parent[i] = i

for node in nodes:
    c, a, b  = node
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += c
print(total- result)