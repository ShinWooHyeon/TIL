# 부품찾기
n = int(input())
shop=list(map(int,input().split()))
m = int(input())
client=list(map(int,input().split()))

# 시간복잡도를 생각한다면 정렬 계속하고 탐색하는거면 nlogN * mlog N
# 근데 정렬은 한번만 한 후 탐색하는거이므로 nlogN + m*logN ==>  o((m+n)logN)
def binary_search(array,target,start,end):
    while start<=end:
        mid=(start+end)//2
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return None
# 안전하게 할거면 리턴값 변수로 지정하고 그거에 대한 if문
shop.sort()
for i in client :
    if  binary_search(shop,i,0,n-1) :
        print('yes',end=' ')
    else:
        print('no',end=' ')
    
# 단순하게 집합을 사용하여도 풀이 가능
n=int(input())
array=set(map(int,input().split()))
m=int(input())
x=list(map(int,input().split()))

for i in x:
    if i in array:
        print('yes')
    else:
        print('no')

# 계수 정렬을 이용하여 풀이시 
n=int(input())
array=[0]*1000001 
for i in input().split():
    array[int(i)] = 1
m=int(input())

x=list(map(int,input().split()))

for i in x :
    if array[i]==1:
        print('yes',end=' ')
    else:
        print('no',end=' ')