from itertools import permutations
from collections import deque
n = int(input())
numbers = list(map(int, input().split()))
cals =[]
cal_count = list(map(int, input().split()))
for i in range(4):
    for j in range (cal_count[i]):
        cals.append(i)
candidates = list(permutations(cals, n-1))
max_value = -1e9
min_value = 1e9

q=deque(candidates)
while q:
    cal = q.popleft()
    result = numbers[0]
    for i in range (n-1):
        if cal[i] == 0:
            result += numbers[i+1]
        elif cal[i] == 1:
            result -= numbers[i+1]  
        elif cal[i] == 2:
            result *= numbers[i+1]
        else:
            if result <0:
                result = -1 * ((abs(result))//numbers[i+1])
            else:
                result //= numbers[i]
    max_value = max(max_value, result)
    min_value = min(min_value, result)

print(max_value)
print(min_value)