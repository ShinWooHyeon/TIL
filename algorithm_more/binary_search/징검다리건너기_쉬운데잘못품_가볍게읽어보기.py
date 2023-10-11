# 징검다리가 있는 개울을 건넌다
# 디딤돌의 숫자는 한 번 밟을때마다 1씩 줄어든다
# 디딤돌의 숫자가 0이되면 그 다음 디딤돌로 한번에 여러 칸 건너 뛸 수 있다
# 다음 디딤돌 여러개면 무조건 가까운 디딤돌을 밟아야 한다
# 최대 몇 명까지 디딤돌 건널 수 있을까?
# 최대 건널 수 있는 사람을 기준으로 이진탐색을 한다
# 즉 이진탐색 시뮬레이션
# 
import copy
def binary_search(stones, start, end, k):
    # end는 stones의 최댓값 start는 0으로 시작한다
    # mid 일때 다 건널 수 있는지 시뮬레이션을 한다
    # 시뮬레이션이 성공하면 start를 mid +1로 증가시키고 search한다
    while start <= end:
        mid = (start+end) //2
        # 시뮬레이션이 성공한다면
        if simulation(stones, k, mid) :
            start = mid + 1
        else:
            end = mid -1
    return mid
def simulation(stones, k, mid):
    stone_simul=copy.deepcopy(stones)
    print(f'시뮬레이션의 mid 값은{mid}')
    for i in range(mid):
        cnt = 0
        for j in range(len(stone_simul)):
            # 건넜을 때 돌이 있으면 돌을 감소시킨다, 건너 뛴 돌의 개수도 초기화시킨다
            cnt +=1 #일단 건너 뛰면 돌의 개수를 추가시킨다
            if cnt > k:
                return False
            if stone_simul[j] > 0 :
                stone_simul[j] -= 1
                cnt = 0
            # cnt가 k보다 작을때는 문제가 아예 안되고 cnt랑 k값이 같은데 마지막 칸인데
            # 0일때 문제가 1되는 1가지 경우는 맨 마지막칸에서 cnt=k 일경우이다
            if j == len(stone_simul) -1 and cnt==k and stone_simul[j] == 0 :
                return False
            # 건넜을 때 돌이 없으면 건너뛰는 돌의 개수에 증가시킨다

            # 마지막 돌에서는 건너뛴돌이 k여도 다음돌로 넘어가야하므로 +1이 더 되기 때문에 false

     # For문을 다 돌았으면 다 건널 수 있는 것이므로
    print('시뮬레이션성공')
    print(stone_simul)
    return True
def solution(stones, k):
    answer = 0
    answer = binary_search(stones, 0, max(stones), k)
    return answer