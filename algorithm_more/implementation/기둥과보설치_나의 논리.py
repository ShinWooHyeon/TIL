'''
def build__delete_height (x, y, answer):
    point=[x, y, 0]
    # 벽면을 벗어나게 설치하는 경우와 겹치게 설치하는 경우는 없다 
    if b == 1:        
        if y==0:
            answer.append(point)
        else:             
            if ([x,y-1,0] in answer) or ([x, y, 1] in answer):
                answer.append(point)
            elif (x-1 >=0) and( [x-1, y, 0] in answer):   # 범위 설정할 필요가 없었던게 인덱스로 들어가는게 아니다!!
                answer.append(point)
    else:
        

    return answer
        
        
        
def solution(n, build_frame):
    answer = [[]]
    building = [[0] * (n+1) for  _ in range(n + 1)]
    for i in build_frame:
        x, y , a, b = build_frame
         
    
    return answer
'''