# 백준 동전 0
N, K = map(int, input().split())
coins =[]
for i in range (N):
    coins.append(int(input()))
coins = coins[::-1]
cnt = 0
now = 0
for coin in coins:
    a = (K-now)//coin 
    if a ==0:
        continue
    now += coin* a
    cnt += a
    if now == K:
        break

print(cnt)

