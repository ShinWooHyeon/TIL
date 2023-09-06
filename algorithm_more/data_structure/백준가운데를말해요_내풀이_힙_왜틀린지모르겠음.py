import sys
import heapq
input=sys.stdin.readline
n= int(input().rstrip())
data=[int(input().rstrip())]
print(data[0])
big=[]
small=[]
middle=data[0]
if n != 1:
    num = int(input().rstrip()) 
    if num >=data[0]:
        heapq.heappush(big ,num)
        heapq.heappush(small, -1 * data[0])
    else:
        heapq.heappush(big ,data[0])
        heapq.heappush(small, -num)
    middle = -1 * small[0]
    print(middle)
# 까지가 처음 big , small에 넣은 형태
# 짝수일때 middle을 큐에 삽입하고 홀수일때는 middle을 저장하고 big, small 개수의 합을 짝수로 유지한다
for i in range (3, n+1):
    num = int(input().strip())
    # i가 홀 수번일때는
    if i % 2 !=0:
        if num >= big[0]:
            heapq.heappush(big, num)
            middle = heapq.heappop(big)
            print(middle)
        else:
            if num >= -1 *small[0]:
                middle= num
                print(middle)
            else:
                middle= -1 * heapq.heappop(small) 
                heapq.heappush(small, -num )   
                print(middle)
    # i가 짝수번일때
    else:
        if num >= middle:
            heapq.heappush(big, num)
            heapq.heappush(small, -middle)
            print(middle)
        else:
            heapq.heappush(small, -num)
            heapq.heappush(big, middle)
            print(num)