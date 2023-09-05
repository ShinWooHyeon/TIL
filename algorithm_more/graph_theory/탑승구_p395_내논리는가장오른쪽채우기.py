# G개의 탑승구 1~ G번 까지의 번호
# P개의 비행기, 차례대로 도착 I번째 비행기를 1번부터 gi 중 하나에 도킹(gi는 1 ~ G), 이미 도킹되어있으면 불가능함
# P개의 배힝그를 순서대로 도킹하다가 어떠한 탑승구에도 도킹 불가능하면 공항운행 중지 , 최대한 많은 비행기 공항에 도킹하고싶다 
# 최댓값을 만들고 싶으면 도킹 가능한 번호중 가장 큰 값에 순차적으로 배치해본다
g = int(input())
p = int(input())
gates=[0] * (g+1)
g_list=[]
for i in range (1, p+1):
    g_list.append(int(input()))
breaker= False
for g_max in g_list :
    if gates[g_max] ==0 :
        gates[g_max] =1
    else:
        while True:
            g_max -= 1
            if g_max ==0:
                breaker =True
                break
            if gates[g_max] == 0:
                gates[g_max] = 1
                break
    if breaker :
        print(sum(gates))
        break