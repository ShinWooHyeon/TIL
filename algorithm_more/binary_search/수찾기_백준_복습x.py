# 백준 수 찾기
n = int(input())
numbers = list(map(int ,input().split()))
numbers.sort()
m = int(input())
checks = list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target,start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

for number in checks:
    if binary_search(numbers, number, 0, n-1) != None:
        print(1)
    else:
        print(0)