# 못생긴 수에 2,3,5를 곱한 수 역시 못 생긴 수 이다
n = int(input())

ugly  = [0] * n
ugly[0] = 1
next2, next3, next5 = 2, 3, 5
i2, i3, i5 = 0, 0, 0
# 1번인덱스부터 n-1 번 인덱스 까지 수를 찾는다
# 가능한 모든 못 생긴수를 2,3,5를 곱하고 min 값을 찾는 식으로 진행하며 오름차순으로 진행 될 수 있도록 한다 
# 1번 인덱스는 2,3,5중 가장 작은 값 만약 1번 인덱스가 next2라면 다음에 고려될 수 있는 수는 그 수에 *2를 한 수
# 모든 인덱스에 2,3,5를 다시 곱한수를 비교해야 한다를 잘 생각해보자
# 2를 
for i in range (1, n):
    ugly[i] = min(next2, next3, next5)
    if ugly[i] == next2:
        i2 +=1 #2가 1번더 고려되야 한다
        next2= ugly[i2] * 2 #
    if ugly[i] == next3:
        i3 +=1 #  *3이 1번더 고려되야 한다
        next3= ugly[i3] * 3 #
    if ugly[i] == next5:
        i5 +=1 # *5가 한 번  더 고려되야 한다
        next5= ugly[i5] * 5 #

print(ugly[n-1])