import sys
from math import ceil
n = int(input())
num_list = list(map(int, input().split()))
b, c = map(int, input().split())
answer = 0
# 응시자가 0인 경우는 없고 총 감독관이 가능한 게 더 많으면 총감독관한테 일단 우선 할당 
if b > c:
    for i in range (len(num_list)):
        if num_list[i] > b:
            num_list[i] -= b
            answer += 1
        else:
            num_list[i] =0
            answer +=1
        # 남은 num_list 요소들을 부감독관 c로 채워야 한다 올림해서 계산한다  
        answer += ceil(num_list[i] / c) 
elif b<c:
    # c가 더 크다면 c로 먼저 채운다음 b에 할당한다 이때 나머지가 0이라면 +1을 해줘 총 감독관 수를 더해준다
    for i in range (len(num_list)):
        # c로 먼저 채운 몫을 구한다 , 이때 몫이 0이라면 총감독관 1명으로 채울 수 있다면 1, 없다면 2가 된다
        # 부감독관 1명으로 다 채울 수 있다면? 총 감독관 1명으로 채울 수 있는지 없는지를 보고 1명,2명을 판단해야 한다
        x = num_list[i] // c 
        y = num_list[i] % c 
        if x ==0 :
            # 이 값이 1보다 크다는 것은 1명으로 다 못 채운다는 것
            if ceil(num_list[i]/b) > 1:
                answer += 2
            # 1명으로 다 채울 수 있으면 총감독관 1명만 들어가면 된다
            else:
                answer += 1
        else:
            # 부감독관으로 다 채우지 못 할 경우 부감독관에 먼저 전부 할당한다. 이때 나머지가 0으로 나올 경우 총감독관수를 +1 해줘야한다
            answer += x #부감독관에 할당된 수를 먼저 더해준다
            # 부감독관에 할당한 후 나머지가 총감독관 감시수보다 작거나 같다면 +1, 크다면 +2
            if y <= b:
                answer +=1
            else:
                answer += 2

'''         
                ㅑf x == 0:

            if ceil(y/b) > 1:
                answer += 2
            else:
                answer += 1
        else:   
            answer += x 
            # c로 먼저 채웠을 때 나머지가 없다면 총감독관 수를 +1 해주고
            if y == 0 :
                answer += 1
            # 나머지가 있다면 총 감독관수로 채우고 총 감독관수로 못 채운다면 부감독관의 수가 한 명더 필요하다
            else:
                if y //b > 1:
                    answer += 2
                else:
                    answer += 1
    
else:
    for i in range (len(num_list)):
        answer += ceil(num_list[i]/b)
'''
print(answer)