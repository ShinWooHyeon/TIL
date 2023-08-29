# 이진 탐색
- 순차 탐색: 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법
- 리스트 내의 count 메소드를 이용할 때도 순차 탐색이 수행된다. N개 일때 최대 N번의 비교연산을 하므로 시간복잡도는 최대 O(N)이다
```python
def sequential_search(n,target,array):
    for i in range(n):
        if array[i]==target:
            return i+1
```

- 이진탐색이란 반으로 쪼개면서 탐색하는 것이다. `배열이 이미 정렬되어 있다면` 매우 빠르게 데이터를 찾을 수 있다.
- 위치를 나타내는 변수 3개를 사용 시작점, 끝점, 중간점을 이용해 `찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교` 원하는 데이터를 찾는다.
- 예시 > 0 2 4 6 8 10 12 14 16 18 의 정렬된 데이터중 4인 원소를 찾는다
    1. 시작점과 끝점을 확인 후 중간점을 정한다(index) 중간점이 실수면 소수점을 버린다. 이 문제에서는 [0]-시작, [4]-중간 [9]- 끝이다
    2. 중간점의 데이터 8과 찾으려는 값 데이터 4를 비교한다. 중간점 데이터가 더 크므로 끝점을 중간점 바로 이전점 [3] 으로 옮긴다.
    3. 시작점이 [0], 끝점이 [3] 이므로 중간점은 [1]이다 (0.5를 버려서), 중간점 데이터의 값이 2이고, 2가 찾으려는 데이터보다 더
       작으므로 2이하의 값은 확인할 필요가 없다. 따라서 시작점이 [2]가 된다. 
    4. 현재 시작점이[2] ,끝점이[3]이다 중간점은[2]이므로 [2]와 찾으려는 데이터값을 비교하면 4가 나오고 탐색을 종료한다 
- 이진탐색의 시간복잡도는 O(logN)이다
```python
#재귀함수를 이용한 이진탐색
# 재귀함수 이용 이진 탐색 소스코드
def binary_search(array,target,start,end):
    if start>end:
        return None
    mid=(start+end)//2 # 몫 계산을 통해 소숫점을 버린다
    if array[mid]==target:
        return mid
    elif array[mid]>target:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)

# 원소의 개수와 찾으려는 target 입력받기
n, target=map(int,input().split())
#행 받고 
array=list(map(int,input().split()))

result=binary_search(array,target,0,n-1) #인덱스이므로 0과 n-1
if result==None:
    print('해당원소는 없다')
else:
    print(result+1) #인덱스이므로 3이면 4번째 원소이다 
```

```python
#반복문을 이용한 이진탐색
def binary_search(array,target,start,end):
    while start<=end:
        mid=(start+end)//2
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return None # 재귀함수와 동일 while문 자체가,즉 start end가 성립이 안되면 아무것도 반환 x 
# 원소의 개수와 찾으려는 target 입력받기
n, target=map(int,input().split())
#행 받고 
array=list(map(int,input().split()))

result=binary_search(array,target,0,n-1) #인덱스이므로 0과 n-1
if result==None:
    print('해당원소는 없다')
else:
    print(result+1) #인덱스이므로 3이면 4번째 원소이다 
```
- 코딩 테스트의 경우 탐색 범위가 큰 상황에서 이진탐색을 자주 사용한다 . 탐색범위가 1000만~2000만을 넘어가면 O(logN)의 속도가 필요한 경우가 많기 때문 

## 트리 자료 구조
- 데이터 베이스는 대용량 데이터 처리가 적합한 트리 자료구조를 이용하여 정렬되어 있다. 
- 트리는 부모 노드와 자식 노드의 관계로 표현된다.
- 트리의 최상단 노드 = 루트노드
- 트리의 최하단 노드 = 단말노드
- 트리의 일부를 떼어내도 트리구조 (이 구조를 `서브트리`라고 한다)
- 트리는 파일 시스템과 같이 계층적이고 정렬된 데이터를 다루기에 적합하다. 
### 이진탐색 트리
- 트리 구조중 가장 간단한 형태로 이진 탐색이 동작할 수 있도록 고안된 자료구조이다.
- `부모노드보다 왼쪽 자식이 작고, 부모 노드보다 오른쪽 자식 노드가 더 크다.`
- 이진탐색 트리에서 데이터를 조회하는 과정은 다음과 같다. 

## 데이터가 너무 길 경우 빠르게 입력받기
- 데이터의 개수가 많은 경우 input()함수를 쓰면 동작속도가 느린 문제가 발생한다. sys 의 stdin.readline() 함수를 사용한다
- rstrip()함수를 통해 줄 바꿈 기호를 없애줘야 한다. 
