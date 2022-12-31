# 점프투 파이썬 복습

## 1. 프로그래밍의 기초, 자료형
- 숫자형
```python
a=173 # 정수형
a=1.2 # 실수형
a= 4.24 E10 / a=4.24e-10 #컴퓨터식 지수표현\

a**b #a의 b제곱
a%b #a를 b로 나눈 나머지
a/b #a를 b로 나눈 몫
```

 &nbsp;

- 문자열 자료형
```python
'Hello' , "hello", """hello"""
 # 큰따옴표, 작은따옴표, 큰 따옴표or 작은따옴표 3개로 둘러싼 형태
'Pyhton\'s hello' #백슬래시를 따옴표 앞에 스면 문자열에 포함가능

multiline="Life is too short\n Go python" #\n 사용하여 줄바꿈
```
- 문자열 인덱싱
```python
a='Hello' , a[1]= 'e'  # 문자열 인덱싱, 0부터 숫자를 센다!
a[-1]='o' #뒤에서 n번째 수
a[0:4] = 'Hell' # 문자열 슬라이싱 시작번호~ 끝번호 ,끝번호는 포함x
```
- 문자열 포매팅
```python
"I eat %d apples." %3 #'I eat 3 aplles' , 숫자열 바로대입
"I eat %s apples." %five #'I eat five apples.
#2개 이상 포맷팅
number=10, 
day='three'
"I'm %d . i was sick for %s days." %(number,day)  

"I'm {0}.i was sick for {1}days." %(number ,day)

```
Tip : %s는 어떤 형태의 값이든 변환 가능

(참고 : 정렬, 공백, 소수점 표현은 한 번 읽어만 보기)

- f 문자열 포매팅
``` python
name='우현'
age=24
f'나의 이름은{name}입니다. 나이는{age}입니다.
#딕셔너리에서도 활용 가능 
```
- 문자열 관련 함수
    - a.`count`('b') = b의 개수 세기
    - a.`find`('b') = b의 위치(처음) 알려주기기 (a.index와 동일하나 index는 없으면 오류 )
    - ".".`join`('abcd')  = 문자열 각 사이에 ,삽입 => 'a,b,c,d 리스트나 튜플에도 자주 사용
    - upper (대문자)/ lower(소문자)/ strip(공백지우기)
    - a.`replace` ("바꿀 문자열, 바뀔 문자열) 문자열 안의 특정한 값 다른값으로 치환
    - a.`split`() => 공백을 기준으로 문자열 나눈다 (괄호 안 기준으로)
        ex. a='Nice to meet you' , a.split()=['Nice','to','meet','you']

### 리스트 자료형
- 리스트 역시 문자열과 동일하게 `인덱싱, 슬라이싱 `가능
- 리스트 덧셈은 문자열 처럼 단순하게 이어짐 [1,2]+[3,4]=[1,2,3,4]

#### 리스트의 수정과 삭제
- a[n]=2 등으로 a[n]요소 값 수정 가능 
- del a[n] 등으로 a[n] 요소 값 삭제 가능
- a.append(x) 리스트 a의 마지막에 x 추가 
- a.sort() 리스트 정렬 
- a.insert(x,y) a[x]값에 y삽입
- a.pop(x) 리스트의 맨마지막 요소를 돌려주고 그 요소 삭제 
- a.count (x): x개수 세기
- a.extend(x) 리스트만 x자리에 올수 있다, 리스트를 더한다 


### 튜플 자료형
- 리스트는 []로 둘러 싸여있지만 튜플은 ()로 둘러 싸임
- 리스트와 달리 튜플은 그 `값을 바꿀 수 없다`
- 나머지 개념은 리스트와 동일

### 딕셔너리 자료형
- {Key1 : Value 1, Key2 : Value 2...}
- 딕셔너리 쌍 추가하기
``` python
a={'1:b'}
a[2]='c'
a= {1:'b',2:'c'}
```
- 딕셔너리 요소 삭제는 key를 지정하여 삭제하면 <del a[1]> 그 key 가지는 key-value쌍 삭제
#### 딕셔너리 관련 함수
- a.`keys`() : a의 key만 모아서 dict_ketys([1,2]) 라는 객체로 돌려준다
(list로 만들고 싶을 경우 list(a.keys())
- a.`values`() : a의 value만 모아서~ 위와 동일
- a.`items`() : Key,Value 쌍을 얻을 수 있다 
- a.`get`(x,'디폴트값'): 딕셔너리 안에 x 있는지 조사, 없으면 디폴트값 반환
- 'x' in a : 해당 key가 딕셔너리 안에 있는지 조사 True or False  bool 형태로 반환

### 집합 자료형
- s1= set([1,2,3]) 같이 `set` 키워드 사용해 만들 수 있다  s1~ {1,2,3}
- s2 = set("Hello")와 같이 문자열을 입력하여 만들 수도 있다 {'e','h','l','o'}
- 집합 자료형의 특징: `중복을 허용x` + `순서가 없다`

#### 교집합, 합집합, 차집합 구하기
- 교집합 = s1 & s2 
- 합집합 = s1|s2 
- 차집합 = s1 - 2
#### 집합 자료형 관련 함수
- s1.add(x) : 값 1개(x) 추가하기
- s1.upade([4,5,6]): 여러개의 값 추가 
- s1.remove(x) : 특정 값(x) 제거

### 불 자료형
- True 참 / False= 거짓
- 자료형의 참과 거짓
    - 문자열 : `"Python"` -True/ `""`- False 
    - 리스트 : `[1,2,3]`- True/ `[]` -False
    - 튜플 : `()` -False
    - 딕셔너리 :`{}` - False
    - 숫자형 : 0이 아닌 숫자 - True/ 0 - False
    - None: False 

### 자료형의 값을 저장하는 공간 변수
- 파이썬에서 변수=객체 
- 리스트 복사시
    - a=[1,2,3], a=b하면 b와 a는 완전히 동일 (주소값도) , 즉 a is b는 True ,a[1]=4하면 b도 바뀐다
    - [:] 사용해서 복사시 a와 b는 서로 영향 x ,동일하지 않다
    - copy 모듈 사용 b=copy(a) , b is a는 False


## 프로그램의 구조를 쌓는 제어문!
### if 문
- if 문 :조건문이 참이면 if문 바로 다음문장 수행, 거짓이면 else문 사용, else문은 if문 없이 독립적으로 사용할 수 없다
- `들여쓰기` :