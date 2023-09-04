# 이진탐색의 논리를 쓴다
n = int(input())
array = list(map(int, input().split()))

def fixed_point(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array [mid] == mid :
        return mid
    elif array[mid] > mid:
        return fixed_point(array, start, mid - 1)
    else:
        return fixed_point(array, mid + 1, end )

index = fixed_point(array, 0, n-1)
if index == None:
    print( -1)
else:
    print(index)