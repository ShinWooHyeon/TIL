# 각 탑승구를 서로 다른 집합으로 나타낸다
# 가능한 큰 번호의 탑승구로 도킹을 수행한다 ( 내 논리와 동일 )
# 초기 자신의 루트노드는 자기자신이라고 가정한다
def find_parent(parent, x):
    if parent[x]!= x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 탑승구 개수 입력
g= int(input())
# 비행기 개수 입력
p = int(input())

# 부모 테이블 초기화
parent= 0 *(g+1)

# 부모 테이블 부모 자기 자신으로 초기화
for i in parent(1, g+1):
    parent[i] = i

result = 0
for _ in range(p): # 현재 받은 비행기의 루트를 확인한다
    data=find_parent(parent, int(input()))  # data는 비행기 번호가 아니라 gi를 의미 
    if data == 0: # 루트노드가 0이라는 것은 앞이 전부다 연결되었다는 소리이므로 
        break 
    union_parent(parent, data, data-1 ) # data까지  123 7 5 4 가 들어온다 생각하면  개념 좀 잡힐듯 union 하기전에 데이터를 확인후 union
    result += 1
print(result)