# 정렬된 배열에서 특정 수의 개수 구하기
from bisect import bisect_left, bisect_right
n , x = map(int, input().split())
array = list(map(int, input().split()))

def count_x(array, x):
    cnt= 0
    left_index = bisect_left(array, x)
    right_index = bisect_right(array, x)
    return right_index-left_index
if count_x(array, x) !=0:
    print(count_x(array, x))
else:
    print(-1)