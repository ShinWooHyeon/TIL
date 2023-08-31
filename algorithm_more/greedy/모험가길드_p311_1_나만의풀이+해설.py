N = int (input())

members=list(map(int, input().split()))

# 공포도가 1인 모험가는 스스로 그룹을 꾸리는 것이 그룹수의 최댓값을 증가시킨다
members.sort(reverse=True)
print(members)
cnt=0
while members:
    a = members.pop()
    num=1
    if a==1:
        cnt+=1
        print(cnt,members)
        continue
    if len(members) <a-1:
        break
    while members:
        x = members.pop()
        num+=1
        if x>a:
            a = x
        
        if a == num:
            cnt+=1
            print(cnt, members)
            break
    if members==[]:
        break
print(cnt)
#----------------------------------------
# 해설 풀이
# 오름차순 정렬은 포인트 완료
N = int (input())

members=list(map(int, input().split()))

# 공포도가 1인 모험가는 스스로 그룹을 꾸리는 것이 그룹수의 최댓값을 증가시킨다
members.sort()

# 그룹수 카운트
cnt = 0

# 그룹에 포함된 수 (여기 까지도 동일하게 잘 설정함) / 초기화 방식을 너무 복잡하게 구현함 !!
num = 0 

for i in members:
    num+=1
    if i== num:
        cnt+=1
        num=0

print(cnt)

