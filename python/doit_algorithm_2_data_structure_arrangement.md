# 기본 자료구조와 배열
## 자료구조와 배열
배열을 사용할 경우 따로 흩어진 변수를 `하나로 묶어서` 사용할 수 있다.
- 배열
    - 묶음 단위로 값을 저장하는 자료구조
    - 객체가 저장되며 각각을 원소라고 함
    - 각 원소는 0,1,2순으로 인덱스를 부여 받는다
    - 배열 원소 자료형은 상관 없으며, 배열 원소 자체를 배열에 저장할 수 도 있다
```python
#실습 2-1
s1=int(input())
s2=int(input())
s3=int(input())
#이렇게 입력받아 각각점수 저장할 경우 학생 수 달라지면 코드 자체도 바뀌어서 불편함
```
### 리스트와 튜플 (둘 모두 데이터 컨테이너)
- 리스트
    - 리스트는 원소 변경 가능한 `mutable` list형 객체 
    - 리스트는 list()로도 작성 가능 , 정수 범위 list는 range()
    - 원솟값을 정하지 않는 list는 None 이용해서도 생성 가능
    - 내포 표기 생성 가능 (list=[a*2 for a in numbers]) , 리스트 안에서 for문이나 if문을 사용하여 새로운 리스트 생성
```python
list1=list() #[] 빈 리스트
list2=list('abc')#['a','b','c']
list3=list([1,2,3]) #[1,2,3] 튜플 집합에도 적용 가능하다
list4=list(range(4))#[0,1,2,3]
list5=[None]*3 #[None,None,None] , 원솟값 정하지 않고 개수만 정할 수 있다.
```
- 튜플
    - 튜플은 원소 변경 불가능한 `immutable` 자료형
    - 맨 마지막 원소 뒤에 쉼표 쓸 수 있으며, 결합 연산자 ()도 생략 가능
```python
tuple1=() #빈튜플
tuple2=1, # (1,) 튜플
tuple03= (1,) #(1,)튜플
# tuple 1,tuple 2 원소 1개면 반드시 튜플 입력해야 한다, 입력하지 않으면 변수로 인지하기 때문
tuple4=1,2,3, #(1,2,3) 여기서는 튜플 내 마지막 쉼표 사라진다
tuple08='a','b','c', #('a','b','c')
tuple=tuple([1,2,3]) #(1,2,3)튜플 역시 리스트, 집합에서 튜플 만들 수 있다.
```

- 리스트와 튜플 풀어내기= 좌변에 변수 우변에 리스트 놓으면 변수에 원소 한번에 대입 가능
```python
x=[1,2,3]
a,b,c=x
print(a,b,c) #1 2 3
```
- 인덱스로 원소 접근하기 
    - s[i:j] = s[i]부터 s[j-1]까지 나열
    - s[i:j:k] = s[i]부터 s[j-1]까지 k씩 건너뛰며 나열 (i또는 j가 len(s)보다 클 경우 len(s)가 지정)
    - 생략패턴 정리
        - s[:] = 리스트 s의 모든 원소 출력 
        - s[:n] = 리스트의 s의 원소 중 맨앞에서부터 n개만 출력
        - s[i:] = 리스트의 원소 중 s[i]부터 끝까지 출력
        - s[-n:]= 리스트의 원소 중 맨끝에서부터 n개까지 출력
        - s[::k]= 리스트의 원소 중 맨 앞에서부터 k개씩 건너가며 끝까지 출력
        - s[::-1]= 리스트 s의 원소 중 맨 끝에서부터 전부 출력
#### 보충학습 파이썬의 자료형
- 뮤터블 자료형 : 리스트, 딕셔너리, 집합 값을 변경할 수 있다
- 이뮤터블 자료형: 수,문자열, 튜플 등이 있으며 값을 변경할 수 없다.
```python
x=0
type(x+17) #int 형
type(x=17) # expression 오류발생
```

#### 보충학습- 등가성과 동일성
- 등가성 비교는 `==`을, 동일성 비교는 `is` 사용.
- 등가성 비교는 좌변과 우변의 값이 같은 지비교, 동일성 비교는 값을 물론 `객체 식별 번호`도 비교
- 비교연산자로 배열의 댜소 또는 등가 판단
    - 맨 앞원소부터 차례로 비교, 원소 값이 같으면 다음원소비교, 어느 원소값 그 배열이 큰 걸로 판단 
    - 배열원소수 다르면 원소수 많은 배열이 더 크다

### 자료구조의 개념
- 자료구조: 데이터 단위와 데이터 자체 사이의 물리적 또는 논리적인 관계로 이루어진 데이터 구성

## 배열이란?
**배열을 사용하는 기본 알고리즘**
- 배열 원소의 최댓값 구하기 
```python
maxi=a[0]
if a[1]>maxi: maxi=a[1]
if a[2]>maxi: maxi=a[2]
#위 과정을 함수로 풀면
from typing import Any, Sequence
# 건너받는 a는 시퀀스형이며 반환하는 것은 임의의 자료형 Any 입니다.
def max_(a:sequence)->Any:  
    maxi=a[0]
    for i in range(1,len(a)):
        if a[i]>maxi: maxi=a[i]
    return maxi
if __name__=='__main__':
    print('배열의 최댓값을 구합니다')
    num=int(input('원소수를 입력하세요: '))
    x=[None]*num
    
    for i in range(num):
        x[i]=int(input(f'x[{i}]값을 입력해주세요'))
    print(f'최댓값은 {max_(x)} 입니다')

```
위 코드의 해석
- 주석과 자료형 힌트
    - Any는 제약이 없는 자료형, Sequence는 시퀀스형(리스트형,바이트 배열형,문자열 형, 튜플 형, 바이트형)
    - 함수 안에서 Any를 반환하므로 배열 a의 원솟값은 변경되지 않는다
    - 호출하는 쪽이 넘겨주는 자료는 시퀀스형이라면 모두 상관이 없다
    - 인수의 원소를 비교 연산자로 비교할 수 있다면 int,float형이 섞여도 상관없다
    - 최댓값이 int면 int 반환 float이면 float형 값 반환
    - max_ 함수에서 매개변수에 대한 함수 어노테이션은 시퀀스 형이 아닌 뮤터블 시퀀스라고 명시한다 (좀 더 공부 필요)

- 재사용할 수 있는 모듈 작성하기
    - 모듈= 파이썬에서 하나의 스크립트 프로그램, 확장자(.py) 포함하지 않는 파일 이름이 모듈의 이름
    - 피연산자 '__ name __'은 모듈 이름을 나타내는 변수이며 작성 규칙은 다음과 같다
&nbsp; 

1. 스크립트 프로그램이 직접 실행될 때 변수 __ name __ 은 `__ main__` 
&nbsp;

2. 스크립트 프로그램이 임포트될 때 변수 __ name __ 은 `원래의 모듈 이름` 

```python
# max 모듈을 만들고 특정 단어 입력 전까지 원소를 입력받고 최댓값 구하기
from max import max_
print('배열의 최댓값을 구합니다')
print('End를 입력하면 종료합니다')
x=[]
n=0
while True:
    s=input(f'x[{n}]값을 입력하세요 ')
    if s=='End':
        break
    else:
        x.append(int(s))

print(f'최댓값은 {max_(x)}입니다.')

# 튜플, 문자열, 리스트등에서도 최댓값 구할 수 있다, 튜플은 리스트와 동일하므로 생략
s='string'
max_(s) # 가장 큰 문자코드 t가 출력
a=['DTS','AAC','FLAC'] 
max_(a) # 가장 큰 문자코드 FLAC 출력
```

#### 보충학습- 리스트와 튜플
- 따로 따로 생성한 리스트와 튜플의 동일성 판단
```python
list1=[1,2,3,4,5]
lsit2=[1,2,3,4,5]
print(list1 is list2) # False , 둘 모두 literal(고정된 값)이 아니기 때문
```
- 리스트, 튜플의 대입
```python
list1=[1,2,3,4]
list2=list1
print(list1 is list2) #True
list2[2]=9
print(list1) # [1,2,9,4]
print(list2) # [1,2,9,4]
# list2=list1은 list1(참조하는 곳의 리스트)를 참조, 따라서 list1과 list2 모두 같은 실체(객체) 참조 , list1에서 바꿔도 list2의 원소도 바뀐다

```
- 리스트 스캔 (튜플과 동일)
```python
x=['아이유','이지은','이지금']
for i in range(len(x)):
    print(x)  # 단순 리스트 요소만 볼때
for i,name in enumerate(x):
    print(f'x{i} = {name}') # x[0]= 아이유 x[1]=이지은 이런식으로 출력
```

### 배열 원소를 역순으로 정렬하기
- a=[2,5,1,3,9,6,7] 이런식이면 a[0]와 a[6] 을 교환... 원소교환 횟수는 원소수//2
```python
from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> Any:
    n=len(a)
    for i in range(len(a)//2):
        a[i],a[-i-1] = a[-i-1],a[i] 
     

if __name__=='__main__':
    nx=int(input('원소수를 입력하세요'))
    x=[None]*nx
    for i in range(len(x)):
        x[i]=int(input(f'x[{i}]값 입력'))
    reverse_array(x) 
    print(x)   
```
- a.reverse()로 리스트 역순 배열 가능(튜플은 immutable이므로 불가),
- revresed(x) s는 x의 원소를 역순으로 하는 이터러블 객체 생성 

### 기수 변환하기(n진수 구하기)
```python
# 내 풀이
def twoj():
    n=int(input('숫자를 입력해주세요'))    
    x=int(input('몇 진수로 바꾸실건가요?'))
    y=n
    s=''   
    while n!=0:
        a=n%x
        n=n//x
        s+=str(a)
    ans=s[::-1]
    print(f'{y}를 {x}진수로 바꾼 수는{ans}입니다 ')

twoj()
# 책 풀이
# 위 reverse 함수 이용해서 변환
def card_conv(x:int,r:int)-> str:

    d=''
    dchar='0123456789ABCDEFGHIJKLMANOPQRSTUVWXYZ'
    while x>0:
        d+=dchar[x&r]
        x//=r
    return d[::-1]  
```

#### 보충수업 2-6 함수 사이에 인수 주고받기
```python
def sum_1ton(n):
    s=0
    while n >50:
        s+=n
        n-=-1
    return s 
x=int(input()) # 5대입 가정
print(f'1부터{x}까지 정수의 합은 {sum_1ton(x)}입니다.')

```
- 위 코드를 보면 변수 x의 값은 호출하기전그대로이다. 
- 매개변수 n으로 실제 인수 x의 값이 복사 된 것이 아니다. 매개변수에 실제 인수가 대입된다.
- x가 대입된 n은 같은 값 5를 참조, 실제 인수 x의 값이 변경되지 않는 것은 int가 이뮤터블 타입이기 때문이다.
![함수 실행 종료 변수](https://user-images.githubusercontent.com/118239192/211506794-fc450805-c368-4e9d-8e82-ba1385c55425.jpg)

- 파이썬에서 인수 전달은 실제 인수인 객체에 대한 참조를 값으로 전달하여 매개변수에 대입 (다른 프로그래밍 언어는 실제 인수의 값을 매개변수에 복사 혹은 매개변수에 복사하는 값에 의한 호출을 사용)
- 파이썬 공식 문서에서는 객체 참조에 의한 전달이라는 용어 사용
- 함수의 실행 시작시점 매개변수는 실제 인수와 같은 객체 참조, 함수에서 매개변수의 값을 변경하면 인수의 형에 따라 다음와 같이 구분한다. 
    - 인수가 이뮤터블일때 : 함수안에서 매개변수의 값을 변경하면 다른 객체 생성하고 그 객체에 대한 참조로 업데이트, 매개변수의 값 변경해도 호출하는 쪽 인수에는 영향을 주지 않음
    - 인수가 뮤터블일때: 함수쪽에서 매개변수의 값을 변경하면 객체 자체를 업데이트, 따라서 매개변수의 값을 변경하면 호출하는 쪽 실제 인수도 값이 변경된다.
```python
def change(lst, idx, val):
    lst[idx]=val
x=[11,22,33]
print('x= ',x)
index=int(input()) # 1
value=int(input()) # 77
change(x,index,value)
print('x= ',x) #[11, 77, 33]
```

### 소수 나열하기 
```python
# 내코드
a=int(input())

ans=[]
for i in range(2,a+1):
    
    for k in range(1,i+1):
        s=0
        x=i/k
        if round(x)==x:
            s+=1
    if s==2:
        ans.append(i)
print(ans)    # 상당히 안좋은 코드 반복을 무려 500499
# 책 코드
counter=0
for n in range(2,1001):
    for i in range(2,n):
        counter+1=1
        if n%i==0:
            break
    else:
        print(n) 
print(c)    # 78022번 break구문통해 어느정도 반복 감소
```
위 코드에서 2,3으로 안나누어 떨어진것을 확인했다면 6과 4로도 안 나누어 떨어진다는 것을 알 수 있다. 
```python
c=0
pt=0
prime=[None]*500 # 소수는 짝수안되니까 max 500개 일것이다
prime[pt]=2
pt+=1
for n in range(3,1001,2): #짝수는 무시하고 홀수만 확인한다. 
    for i in range(1,pt):  # 찾은 소수로만 나눗셈한다 나머지들은 다 소인수분해 느낌, 다 표현가능
        c+=1
        if n%prime[i]==0:
            break
    else:                 # 찾은 소수들로 안나누어 떨이지면 그게 바로 새로운 소수
        prime[pt]=n
        pt+=1
for i in range(pt):
    print(prime[i])
print(c) # 14622번으로 5분의 1로 줄음
```