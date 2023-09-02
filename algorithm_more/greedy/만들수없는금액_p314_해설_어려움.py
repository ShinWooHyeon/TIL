# 만들 수 없는 금액 (풀이 실패 해설만)
# 1부터 target -1 까지 모든 금액을 만들 수 있다고 가정, target 금액을 만들 수 있다면 target 값을 업데이트 한다 
n = int(input())
coinlist=list(map(int,input().split()))
coinlist.sort()

target=1
# 각 단계에서 동전을 확인할 때마다 자기자신까지 만들 수 있고 자기자신이 동전이 있으므로 최대 자기자신+동전이 target이 되는 것이다 
for i in coinlist:
    if target < i :
        break
    target+=i

print(target)
