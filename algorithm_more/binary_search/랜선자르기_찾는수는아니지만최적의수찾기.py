# 이상적인 최대 정수 구한다
k, n = map(int,input().split())
lines=[]
total =0
for _ in range(k):
    a= int(input())
    lines.append(a)
    total += a

end = total //n + 1
def binary_search(lines, target, start, end):
    if start >  end:
        return None

    mid = (start + end)// 2
    mid2 = mid + 1
    result = 0
    result2 = 0    
    for line in lines:
        result += line//mid
        result2 += line//mid2
    if result >= target and result2 < target:
        return mid
    if result >= target:
        return binary_search(lines, target, mid+1, end)
    else:
        return binary_search(lines, target, start, mid -1)

print(binary_search(lines, n, 0, end))