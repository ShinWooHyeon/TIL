from collections import deque
# 노드 개수만 일단 입력받는다
n = int(input()) 

# 모든 노드에 대한 진입차수는 0으로 초기화 한다
indegree=[0] * (n+1)
# 강의 시간에 대한 리스트를 생성한다
lec_time=[0] * (n+1)

# 각 강의 노드에 소요된 시간을 기록하는 리스트를 생성한다
lec_arrive=[0] * (n+1)

# 간선정보 입력받기 위한 리스트
graph=[[] for _ in range (n+1)] 

# 간선 정보를 입력 받는다 (이때 입력받는 순서가 강의번호이고 )

for i in range (1 , n+1):
    lecture=list(map(int, input().split()))[:-1]
    lec_time[i] = lecture[0]
    if len(lecture) >=2:
        for j in lecture[1:]:
            graph[j].append(i)
            indegree[i]+=1


def topology_sort():
    result = []
    q = deque()

    # 진입차수가 0인 노드를 큐에 삽입한다 
    for i in range(1, n+1) :
        if indegree[i]==0:
            q.append(i)
            lec_arrive[i]=lec_time[i]
    # 큐가 빌 때까지 반복한다
    while q:
        # q에서 원소 꺼내기
        now = q.popleft()
        result.append(now) 
        # now는 진입차수가 0이된 노드, 0이된 노드에서 시작하는 간선을 모두 제거한다.
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i]==0:
                lec_arrive[i]=lec_time[i] + lec_arrive[now]            
                q.append(i)

    for i in range( 1, len(lec_arrive)):
        print(lec_arrive[i])

topology_sort()
