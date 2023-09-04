# 1. 쿼리 리스트에서 꺼낸다
# 2. 꺼낸 쿼리의 접두사나 접미사를 확인한다

def qm_index(query):
    # 2-1 접두사가 ?라면 binary search를 하는데 찾은게 ? 면 오른쪽 찾고 찾은게 숫자면 왼쪽찾기
    n = len(query) 
    if query[0] == '?':
        start = 0
        end = len(query) - 1
        while start<= end:
            mid = (start + end) //2
            # 쿼리의 마지막 인덱스이거나 다음행이 ?가 아닐경우 
            if (mid == n-1 or query[mid +1] !='?')  and query[mid] == '?':
                result = (0, mid)
                break
            # 위 조건없이 ?라면 아직 맨 오른쪽 ?가 아닌 경우이므로
            elif query[mid] =='?':
                start = mid + 1
            else:
                # ?가 아니라면 ,즉 단어를 발견했다면 왼쪽을 서치해야함
                end = mid -1 
    else: 
        start = 0
        end = len(query) - 1
        while start<= end:
            mid = (start + end) //2
            # 쿼리의 처음 인덱스이거나 앞이 ?가 아닐경우 
            if (mid == 0 or query[mid -1] !='?')  and query[mid] == '?':
                result = (mid, n-1)
                break
            # 위 조건없이 ?라면 아직 맨 왼쪽 ?가 아닌 경우이므로
            elif query[mid] =='?':
                end = mid - 1
            else:
                # ?가 아니라면 ,즉 단어를 발견했다면 오른쪽을 서치해야함
                start = mid +1 
    return result # ?의 인덱스들을 반환한다  
def solution(words, queries):
    answer = []
    for query in queries:
        start, end = qm_index(query)
        cnt = 0
        if start ==0:    
            if end != len(query)-1: #시작과 끝 모두가 ?가 아니라면
                for j in words:
                    if j[end+1:] == query[end+1:]:
                        cnt += 1
            else: # 시작과 끝 모두 ?라면 
                if len(j) == len(query):
                    cnt += 1
        else:    
            for j in words:
                if j[: start ] == query[:start] and len(j) == len(query):
                    cnt += 1
        answer.append(cnt)
    return answer

