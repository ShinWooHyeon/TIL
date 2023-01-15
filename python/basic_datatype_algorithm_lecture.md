# 1강- 기본 자료구조
- 스택 자료구조 : 먼저 들어온 데이터가 나중에 나가는 형식의 자료구조 (선입후출)
- 스택 동작은 삽입과 삭제로 이루어진다 (가장 마지막에 들어온 원소가 삭제)
```python 
stack=[]
stack.append(1) # 스택 자료의 삽입 , 시간복잡도는 상수시간
stack.append(2)
stack.pop() # 스택 자료의 삭제
print(stack[::-1])# 최상단 원소부터 출력
```
- 큐 자료구조: 먼저 들어온 데이터가 먼저 나가는 형식의 자료구조(선입선출) , 입구와 출구가 모두 뚤려 있는 형식 ,  일종의 대기열이라고도 볼 수 있다
```python
from collections import deque
queue=deque()
queue.append(5) #리스트의 append와 동일, 시간복잡도는 상수시간
queue.append(3)
queue.popleft()   #deque([3])
print(queue)
queue.reverse()
```

# 2강 우선순위 큐
- **우선순위 큐**:우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조
    - 스택: 가장 나중에 삽입된 데이터가 가장 먼저 추출
    - 큐: 가장 먼저 삽입된 데이터가 가장 먼저 추출
    - 우선순위 큐: 가장 우선순위가 높은 데이터가 가장 먼저 추출
- 구현 방식
    - 1. 단순히 리스트를 이용하여 구현 
    - 2. 힙(heap)을 이용하여 구현
- 데이터의 개수가 N개일 때 구현 방식에 따른 시간복잡도
    - 리스트로 구현 : 삽입시간은 O(1), 삭제시간 O(N)
    - 힙으로 구현 : 삽입시간 O(log N),O(log N)
- 즉 단순히 N개의 데이터를 힙에 넣었다가 모두 꺼내는 작업은 정렬과 동일(힙 정렬), 이 경우 시간 복잡도는 O(NlogN)

- **힙(Heap)**의 특징
    - 힙은 `완전 이진 트리` 자료구조의 일종
    - 힙에서는 항상 `루트노드`를 제거
    - 최소 힙(min heap)
        - 루트 노드가 가장 작은 값을 가진다
        - 값이 작은 데이터가 우선적으로 제거
    - 최대 힙(max heap)
        - 루트 노드가 가장 큰 값을 가진다
        - 값이 큰 데이터가 우선적으로 제거

- 완전 이진 트리 :루트 노드부터 시작하여 왼쪽 자식 노드, 오른쪽 자식 노드 순서대로 데이터가 차례대로 삽입 
- 최소 힙 구성 함수 Min-Heapify()
    - 상향식 : 부모 노드로 거슬러 올라가며 부모보다 자신의 값이 작은 경우 위치 교체 
- 힙에 새로운 원소 삽입시, O(logN)의 시간 복잡도로 힙 성질 유지
- 힙에 원소 추가 및 삭제 과정
<img width="761" alt="heap 원소추가" src="https://user-images.githubusercontent.com/118239192/212528292-cba167eb-64fe-4d7c-bd56-871d48bd7e98.png">
<img width="760" alt="heap 제거1" src="https://user-images.githubusercontent.com/118239192/212528348-e53e7a7d-d49e-4163-9136-f6e262225978.png">
<img width="774" alt="heap 제거2" src="https://user-images.githubusercontent.com/118239192/212528351-765cf0c7-19c3-46c7-8450-3a283ce3626b.png">

```python
import sys
import heapq  # 기본 동작 구조는 mean heap 
def heapsort(iterable):
    h=[]
    result=[]
    # 모든 원소 힙에 삽입
    for value in iterable:
        heapq.heappush(h,value)
    # 힙에 삽입된 모든 원소 차례로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq,heappop(h))
    return result
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
    res=heapsort(arr)
for i in range(n):
    print(res[i])
```

# 3강 트리 자료구조
- 트리 :가계도와 같은 계층적인 구조 표현할때 사용하는 자료구조
    - 루트 노드 : 부모가 없는 최상위 노드
    - 단말 노드 : 자식이 없는 노드 (가장 아래쪽 노드)
    - 크기: 트리에 포함된 모든 노드의 개수
    - 깊이 : 루트 노드부터의 거리 (루트노드 =0)
    - 높이 : 깊이 중 최댓 값
    - 차수 - 각 노드의 간선 개수
    - 트리의 크기가 N일 때 전체 간선의 개수는 N-1개이다.
- 이진 탐색 트리 : 이지 탐색이 동작할 수 있도록 효율적  탐색 가능한 자료구조
- **왼쪽 자식노드<부모 노드 < 오른쪽 자식 노드**
- 모든 부모 노드는 왼쪽 자식 노드보다 크고, 오른쪽 자식 노드보다 작다
- 트리의 순회  
    - 트리 자료구조에 포함된 노드를 특정 방법으로 한 번씩 방문
    - 전위 순회 : 루트를 먼저 방문 왼쪽과 오른쪽에 차례로 방문
    - 중의 순회 : 왼쪽 먼저 방문,루트 방문, 이후 오른쪽 방문
    - 후위 순회 : 왼쪽 자식 방문 후 오른쪽 자식 방문, 마지막 으로 루트 방문
<img width="462" alt="트리의 순회" src="https://user-images.githubusercontent.com/118239192/212528715-103cbb01-4be2-4870-9a21-70bc29efd6ec.png">

- 트리의 순회 코드 구현 예제 (트리는 딕셔너리로 표현 가능)
<img width="734" alt="트리 순회 코드 예제" src="https://user-images.githubusercontent.com/118239192/212528830-c9a3c497-e244-403f-86b6-cab0a979bab2.png">

위 코드에 입력 A B C B D E C F G 입력시 트리 순회 결과처럼 나온다

# 4강 특수한 목적의 자료구조: 바이너리 인덱스 트리
- 데이터 업데이트가 가능한 상황에서의 구간 합 문제
- **바이너리 인덱스 트리** : 2진법 인덱스 구조 활용, 구간 합 문제 효과적 해결 가능 (팬윅트리)
- 2진법 으로 7과 -7 표현시  -7은 정수 7의 이진법 표기를 모두 뒤집고 마지막에 +1
- 0아 아닌 마지막 비트 찾는 경우: **K &-K** 계산을 한다 
```python
n=8
for i in range(n+1):
    print(i,"의 마지막 비트 : ",(i&-i))  
```
- 트리구조 만들기: n개의 데이터를 담을 수 있는 배열을 만든다
    - 0이 아닌 마지막 비트= 내가 저장하고 있는 값들의 개수
    - 특정 값 변경 :0이 아닌 마지막 비트만큼 더하면서 구간들의 갑 변경 
    - 바이너리 인데스 트리의 누적합 : 0이 아닌 마지막 비트만큼 빼면서 구간들의 합 계산 가능 (11까지 합 => 11, 9~10, 1~8)
<img width="789" alt="바이너리 인덱스 트리 구현 예시" src="https://user-images.githubusercontent.com/118239192/212529347-82e74c03-8bd4-41d8-a6be-7a94867da6ea.png">

(트리 순회, 바이너리 인덱스 트리 코드 스스로 연습 필요 )

# 5강 선택 정렬과 삽입정렬
- 정렬 : 데이터를 특정한 기준에 따라 순서대로 나열
- **선택 정렬**: 처리 되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것
```python
x=[7,5,9,0,3,1]
for i in range(len(x)):
    min_index=i
    for j in range(i+1,len(x)):
        if x[min_index]>x[j]:
            min_index=j
    x[i],x[min_index]=x[min_index],x[i]
```
- 선택 정렬의 시간 복잡도 : N번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야 함
- 연산 횟수 = N +N-1 +....+2
- 이는 (N**+N-2/)=> 빅오 표기법에 따라 O(N**2)

- **삽입 정렬** : 처리 되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입
- 선택 정렬에 비해 구현 난이도 높지만 일반적으로 효율적임
- 첫 번째 데이터는 정렬되어 있다고 판단, 두 번째 데이터가 어떤 위치로 움직일지 판단.첫 번째 데이터의 왼쪽으로 들어가거나 (이동했는데 왼족보다 더 작으면 계속 왼족 이동) 오른쪽으로 들어가거나 두 경우만 존재한다.
```python
x=-7,5,9,0,3,1
for i in range(1,len(x):)
    for j in range(i,0,-1):
        if x[j]<x[j-1]:
            x[j],x[j-1]=x[j-1],x[j]
        else:
            break
print(x)
```
- 삽입 정렬의 시간 복잡도: O(N**2) 선택 정렬과 마찬가지로 반복문이 두번 중첩되어 사용되기 때문..
- 삽입 정렬은 현재 리스트의 데이터가 거의 정렬된 상태라면 매우 빠르게 동작
- 최선의 경우 O(N)의 시간복잡도

# 6강 퀵 정렬과 계수 정렬
- 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
- 표준 정렬 라이브러리의 근간이 되는 알고리즘
- 가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준 데이터(Pivot)로 설정
- ex. x=[5,7,9,0,3,1,6,2,4,8], 
    - 현재 피벗의 값은 5 왼쪽에서부터 5보다 큰 데이터 선택(7), 오른족에서는 5보다 작은 데이터 선택 (4) 7과 4의 위치를 바꿔준다 .[5,4,9,0,3,1,6,2,7,8]
    - 그후 9와 2를 또 바꿔준다, [5,4,2,0,3,1,6,9,7,8]
    - 6과 1골라진다. 위치가 엇갈리는 경우 작은 데이터와 피벗 값의 위치를 바꿔준다 [1,4,2,0,3,5,6,9,7,8]
    - 이경우 피벗 값 기준으로 왼쪼그오른쪽으로 나뉘어지는 이 과정을 **분할**이라고 한다
    - 왼쪽 기준으로 마찬가지로 퀵 정렬 (즉 재귀적으로 반복)
    - 퀵 정렬이 빠른 이유: 이상적인 경우 분할이 절반씩 일어난다면 전체 연산횟수로 O(NlogN)
    - 높이 :log N(밑이 2), 높이=N  너비*높이= NlogN
- 퀵 정렬은 평균의 경우 O(NlogN)의 시간 복잡도를 가진다
- 최악의 경우 O(N**2)의 시간 복잡도 가질 수 잇다. 
- (첫 번째 원소를 피벗으로 삼고, 이미 정렬된 배열일경우 계속 오른쪽 그대로 남아있기 때문)
```python
x=[5,7,9,0,3,1,6,2,4,8]
def quick_sort(arr,start,end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot=start
    left=start+1
    right=end
    while left<=right:
        #피벗보다 큰 데이터 찾을 때 까지 반복
        while (left<= end and arr[left]<=arr(pivot)):
            left+=1
        while  (right> start and arr[right] >=arr(pivot)):
            right-=1
        if left>right:
            arr[right] ,arr[pivot]=arr[pivot],arr[right]
    quick_sort(arr,start,right-1) 
    quick_sort(arr,right+1,end)
quick_sort(arr,0,len(arr)-1)
print(arrr)
# 파이선의 장점 살린 퀵 정렬
x=[5,7,9,0,3,1,6,2,4,8]
def quick_sort(arr):
    if len(arr)<=1:
        return array
    pivot=arr[0]
    tail=arr[1:]
    left_side=[x for x in tail if x<=pivot]
    right_side=[x for x in tail if x>pivot]
    return quick_sort(left_side)+[pivot]+quick_sort(right_side)
print(quick_sort(array))
```
- **계수 정렬** : 특정한 조건 부합할 때만 사용 가능, 매우 빠르게 동작
    - 데이터 크기 범위 제한되어 정수형태로 표현 할 수 있을때 가능
    - 데이터의 개수가 N,데이터(양수) 중 최댓값 K일때 최악의 경우 수행시간 O(N+K)
- ex 가장 작은 데이터부터 가장 큰 데이터 까지 범위가 모두 담길 수 있도록 리스트 생성  (백준 10989번 문제 사용 개념과 동일)
- 각 인덱스가 데이터의 값, count가 개수
- 출력은 인덱스를 출력 
```python
array=[7,5,9,0,3,1,6]
count=[0]*(max(array)+1)
for i in range(len(array)):
    count[array[i]]+=1
for j in range(len(count)):
    for k in count[j]:
        print(j,end='')
# 데이터의 개수만큼 확인하므로 N개 K만큼 인덱스 확인해야하므로 N+K
```
- 계수 정렬의 시간 복잡도 O(N+K), 정렬 수행할 데이터 N개, K만큼의 크기 가지는 공간 필요 공간복잡도 역시 O(N+K)
- 계수 정렬은 때에 따라서 심각한 비효율성(0과 990000개, 단 2개)
- 계수 정렬은 동일한 값을 가지는 데이터가 여러개 등장 할때 효과적으로 사용할 수 있다