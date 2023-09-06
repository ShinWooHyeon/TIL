# 한 바퀴를 도는 구조며 사라지는 경우 전체 시간의 합과 k를 비교한다
import heapq
def solution(food_times, k):
    if sum(food_times) <= k:
        return -1 # k시간 후 먹을 양이 없는 것을 알 수 있기 때문에
    # 시간이 작은 음식부터 빼야한다면
    q=[]
    for i in range (len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))
    # 현재 시간, 음식번호로 큐에 저장되어있다
    # 현재까지 먹기위해 사용한 시간과 직전에 다 먹은 음식의 시간을 변수로 설정
    sum_value = 0
    previous = 0
    
    length = len(food_times)
    # 현재까지 먹기위해 사용한시간과 곧 큐에서 나올 음식이 완료될때 걸린 총 시간
    # 직전음식까지 걸린시간을 빼주는 이유는 이미 고려했으니까
    # 그런데도 k보다 작다면 큐에서 나올 수 있다는 의미
    while (sum_value) +((q[0][0] -previous) *length) <= k:
        now = heapq.heappop(q)[0] #큐에서 나온 음식, 즉 다 먹을 음식의 시간
        # 직전음식보다 now가 더 앞이고
        sum_value += (now - previous) * length 
        length -= 1
        previous = now # 갱신
    # while문 다 돌고 즉 음식이랑 남은 시간
    # 이제 남은시간과 남은 음식들이있으면 
    result= sorted(q, key = lambda x: x[1])
    return result[(k-sum_value)%length][1]