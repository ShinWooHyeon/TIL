# 이진 탐색을 두 번 해야한다는 떠올렸지만 
# 이 개념은 고난이도 문제에 자주 사용할 수 있는 테크닉
def count_value(array, x) :
    # 데이터 개수를 통해 인덱스 확인
    n = len(array)

    # 처음 나오는 인덱스 계산
    a= first(array, x, 0, n-1)
    if a == None:
        return 0 # 해당하는 인데스가 없다는 것은 원소가 없다는 것
    
    b= last(array, x, 0, n-1)
    # 이상 이하의 개념으로 개수를 셀 때는 +1 해줘야한다
    return b - a + 1 

def first(array, target, start, end):
    if start > end :
        return None
    mid = (start + end)//2
    
    # 이 테크닉이 좀 중요 , 가장 왼쪽 인덱스를 찾는 스킬 mid가 0인경우는  0과 1을 더할 경우 밖에 없다 즉 
    # 즉 mid값을 넣었을때 target값이랑 같으면서  mid는 0이 될때까지 찾는것, why? 가장 왼쪽이여야 하므로 
    # 찾는 수 중에서 가장 왼쪽이므로 mid가 target인데 앞이 target보다 작으면 mid가 가장 왼쪽 인덱스일 수 밖에 없다
    if (mid == 0 or target > array[mid-1]) and array[mid] == target:
        return mid
    # 중간점의 값보다 찾으려는 값이 작거나 같은 경우 
    elif array[mid] >= target :
        return first(array,target, start, mid-1)
    # 중간점의 값보다 찾으려는 값이 큰 경우
    else:
        return first(array, target, mid + 1, end)

def last(array, target, start, end):
    if start> end :
        return None
    mid = (start + end) // 2

    if (mid == n-1 or target < array[mid+1]) and array[mid] == target:
        return mid
    elif array[mid] > target:
        return last(array, target, start, mid - 1)
    else:
        return last(array, target, mid+1, end)
    
n , x = map(int, input().split())
array = list(map(int, input().split()))

# 값이 x인 데이터의 갯수를 센다
cnt = count_value(array, x)

if cnt == 0:
    print(-1)
else:
    print(cnt)