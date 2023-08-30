# 떡볶이 떡 만들기 
# 이진탐색을 해서 
n , m = map(int,input().split())
cake_list=list(map(int,input().split()))
start=0
end=max(cake_list)
ans=0
while (start<=end):
    mid=(start+end)//2
    get_cake=0
    for i in cake_list:
        if i> mid:
            get_cake+=i-mid        
    if get_cake < m:
        end= mid-1
# 포인트는 값이 존재하지 않더라도 12  9 6 5  사이에 7이 목표더라도이더라도 result에  12가 기록되고 이후 9쪽도 보기 때문에 9까지는 기록되지만
# 9가 기록된 다면 당연히 12는 기록되지 않고 6또한 조건을 만족하지 않으므로 조건을 만족할 때 기록하기만 하면 이진탐색으로 더 최적의 조건까지
# 기록하고 return 하기 때문에 동일한 값이 없더라도 문제가 없다
    else:
        ans=mid
        start=mid+1

print(ans)