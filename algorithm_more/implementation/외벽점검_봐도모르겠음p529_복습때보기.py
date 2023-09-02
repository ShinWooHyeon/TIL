# 원형문제의 경우 길이를 2배로 늘려서 일자로 만든다 
from itertools import permutations
def solution(n, weak, dist):
    # 길이를 2배로 늘려서 원형을 일자형태로 변경한다 
    # 트랙의 길이 n만큼을 원래 취약지점에 더해줘야한다
    length = len(weak)  # 취약지점의 개수
    for i in range(length):
        weak.append(weak[i]+n)
    answer = len(dist) + 1 # 최대수+1, 즉 점검 못할 경우 이 값이 갱신이 안되 -1을 return한다
    
    # 취약지점에서 출발한다고 생각하기 때문에 범위가 length가 된다 
    for start in range (length):
        # 친구를 나열하는 모든 경우의수를 각각 확인한다 친구가 dist이므로
        for friends in list(permutations(dist,len(dist))):
            count = 1 #(투입 친구의 수 )
        # 해당 친구가 점검할 수 있는 마지막 위치
        # 시작점을 선택하는 위에서 돌린거고 아래 for문은 고른 친구들의 
        # weak[start]에서 고르고 count가 1이니까 1명만 즉 0번인덱스 친구만 가는것이므로
        position = weak[start] + friends[count -1]
        
        # 시작점부터 모든 취약 지점을 확인한다 (즉 연속된 모든 취약지점 2배로 늘렸기 때문에)
        # for문의 범위는 2배로된 길이중 확인할 1배수 길이를 의미한다
        for index in range (start, start + length):
            # 점검할 수 있는 위치를 벗어난 경우
            # 포지션 까지밖에 못간것 weak[index] 까지 가야하는데 
            if position < weak[index]:
                #친구 추가
                count += 1
                if count > len(dist) : #최대 친구수 넘어가면
                    break
                position = weak [index] + friends[count -1]
        answer = min(answer, count) # 최솟값 계산
    if answer > len(dist):
        return -1
    return answer