import sys
n, m = map( int,input().split())
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

parent=[0]*(n+1)
for i in range(n+1):
    parent[i]=i

def union_parent(parent,a,b):
    if find_parent(parent, a) < find_parent(parent,b):
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]

for i in range (m):
    a, b, c = map(int, input().split())
    if a==0:
        union_parent(parent, b, c)
    else:
        if find_parent(parent, b) == find_parent(parent, c):
            print('YES')
        else:
            print('NO')
