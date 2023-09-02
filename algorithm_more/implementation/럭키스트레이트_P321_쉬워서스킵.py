num = list(map(int,input()))
# 데이터가 n이 최대 1억인데 시간제한 1초 log N이나 절반절반해야댐 
# N을 일일이 확인하는 경우는 메모리 초과 
a=len(num)

if sum(num[:a//2])==sum(num[a//2:]):
    print('LUCKY')
else:
    print('READY')