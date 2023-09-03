# 계수정렬을 쓸지 그냥 정렬을 쓸지 가 일단 고민
# 정렬 한 후에  [1 2 2 2 3 3 4 6]
# 개수 세는 리스트 생성해서 세고
# 실패율 리스트 만드어서 
# 모든 스테이지마다 실패율 계산해서 
# N +1이 스테이지에 있을 경우 깬 사람 수 
def solution(N, stages):
    count_list=[0] * (N + 1)
    answer=[]
    for i in stages:
        if i <= N:
            count_list[i] += 1
    stage_people = len(stages)
    for j in range (1, N + 1):
        now_people = count_list[j]
        fail = now_people/stage_people
        answer.append((fail, j)) 
        stage_people -= now_people
    answer.sort(key = lambda x :(-1 * x[0], x[1]))
     
    return answer
N = 5
stages =[2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))
# countlist = []