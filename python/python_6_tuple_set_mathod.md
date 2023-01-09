# 튜플(Tuple)과 세트(Set)
## Tuple
- 불변한 값들의 나열
- 순서를 가지고 ,서로 다른 타입 요소를 가질 수 있다
- `immutable`(변경불가능),`iterable`(반복가능)
- 소괄호`()`혹은 `tuple()`로 생성 가능

## Set
- `유일한 값`들의 모음(Collection)
- 순서 x, 중복된 값 x
- mutable, iterable (set는 순서가 없기 때문에 반복시 순서 다를 수 있다)
- 중괄호 '{}' 혹은 `set()` 로 생성 가능(빈 set는 set()로만 생성) 
- 순서가 없기 때문에 index 등의 접근은 불가능하다
- set.add()로 추가 , set.remove()로 제거
- set 활용으로 중복된 값 쉽게 제거 가능(순서 중요하면 사용하면 안 된다)

# 데이터 타입과 메서드
문자열.split(), 리스트.append 등 
&nbsp;

### `데이터 타입.메서드()`
메서드는 객체와 연관되어 사용, 사용하고자 하는 대상 `.`으로 연결
- 함수 : 독립적으로 호출 가능
- 메소드 독립적으로 호출 x, 클래스 및 객체와 연관되어 있다

**클래스 및 객체와 연관되어있다 => 메서드,독립적으로 호출 가능=> 함수** 
(함수가 더 큰 개념)

## 문자열 메서드
- 문자열: 문자들의 나열
- 문자열 탐색/검증 메서드 (검즘 메서드, 즉 여부 판단은 True or False 반환)
    - s.find(x) : x의 첫 번째 위치 반환, 없으면 -1 빈환
    - s.index(x): x의 첫 번째 위치 반환, 없으면 Error 발생
    - s.isalpha(): 알파벳 문자 여부(단순 알파벳x, 유니코드 상 letter, 한국어 포함)
    - s.isupper(): 대문자 여부
    - s.islower(): 소문자 여부
- 문자열 변경 메서드
    - s.replace(old,new, count) : 바꿀 문자 새로운 문자로 바꿔 반환
    - s.strip([chars]): 공백이나 특정 문자 제거(값만 반환, 실제 객체 변화x)
    - s.split(sep=None,maxsplit=-1): 공백이나 특정 문자를 기준으로 분리
    - 'seperator'.join([iterable]): 구분자 기준으로 itreable을 합친다
    - s.capitalize():가장 첫 번째 글자를 대문자로 변경
    - s.title(): `'`나 공백 이후를 대문자로 변경
    - s.upper(): 모두 대문자로 변경
    - s.lower(): 모두 소문자로 변경
    - s.swapcase(): 대<-> 소문자 모두 변경
```python
# replace 예시
print('iudlwlrmall'.replace('i','I'))# Iudlwlrmall으로 출력
print('iudlwlrmall'.replace('l','i',2)) #iudwrmall으로 출력

# strip 예시
a=' 와우!!'
print(a.strip('!')) #'  와우'로 출력 , 특정문자 지정해서 제거 가능
print(a.stirp()) # '와우!!'로 출력, 지정 안하면 공백제거
print(a.rstrip()) #'  와우!!'로 출력,오른쪽 공백 제거
print(a.lstrip()) #'와우!!'로 출력, 왼쪽 공백 제거

# split 예시 
print('x,y,z'.split()) #['x,y,z']로 출력
print('x y z'.split()) #['x','y','z']로 출력 ,지정안되있꺼나 공백 시 연속된 공백문자를 단일한 공백 문자로 간주
print('010-1234-5678'.split('-')) # ['010','1234','5678']로 출력

#seperator.join 예시
a=['아','이','유']
print(''.join(a)) #'아이유'로 출력,iterable에 문자이외의 형태 있으면 오류
```

## 리스트 메서드
- 리스트:변경 가능한 값들의 나열된 자료형, mutable,iterable
    - a.append(x):리스트의 마지막 항목에 x 추가
    - a.insert(i,x): 리스트 인덱스 i에 x 추가
    - a.remove(x): 리스트 첫 번째(가장 왼쪽) x 제거, 항목 없으면 Value Error
    - a.pop():리스트 가장 오른쪽 반환 후 제거
    - a.pop(i):리스트의 인덱스 i에 있는 항목 제거 후 반환
    - a.extend(m): 순회형 m의 모든 항목 리스트 끝에 추가
    - a.index (x,start,end): 가장 왼쪽에 있는 x의 인덱스 반환
    - a.reverse():리스트를 역순으로 뒤집는다
    - a.sort(): 리스트 정렬
    - a.count(x): 리스트에서 항목 x 몇개 존재하는지 반환
```python
#리스트 메서드 중 주의 사항
a=['아이유','이지은']
a.insert(10000,'이지금') 
#['아이유','이지은','이지금']리스트길이보다 인덱스 크면 맨 뒤에 추가)
a.remove('이지동') # 없을경우 Value Error
a.index('이지동') # 없을경우 Value Error
#Sort와 Sorted
a=['b','c','a']
x=sorted(a)
print(x)
print(a)        # ['a','b','c']반환/ ['b','c','a'] 반환 원본은 변경 x
b=['나','다','가']
y=b.sort()
print(y)
print(b)       # None  , ['가','나','다] 원본 변경
# reverse
a=['2','1','3']
b=a.reverse()
print(b)
print(a)     # None, ['1','2','3'] 출력
```

## 세트
- 유일한 값들의 모음(collection)
- 세트 메서드
<img width="566" alt="세트메서드" src="https://user-images.githubusercontent.com/118239192/211248786-d5e3e684-c5a1-481a-8bdf-50487922e236.png">

## 딕셔너리
- Key와 Value로 이루어진 쌍의 모음
- key는 불변 자료형만 가능 ,Value는 관계 x
    - d.clear(): 모든 항목 제거
    - d.keys():딕셔너리 d의 모든 키를 담은 뷰를 반환
    - d.values():d.keys():딕셔너리 d의 모든 Value를 담은 뷰를 반환
    - d.get(k): 키 k의 value반환,없으면 None 반환
    - d.get(k,v): 키 k의 value반환, 없으면 v 반환
    - d.pop(k):키 k의 value 반환 및 딕셔너리 d에서 삭제, 없을경우 KeyError
    - d.pop(k,v): 키 k의 value 반환 및 딕셔너리 d에서 삭제, 없을경우 v반환
    - d.update([other]):딕셔너리 d의 값을 매핑하여 업데이트
```python
#get
a={'국힙원탑':'아이유','나의 아저씨':'이지안'}
print(a.get('이지금')) #None
print(a.get('국힙원탑')) # 아이유
print(a.get('이지금',0))# 0
#update(update 안 괄호에서는 ' 제거해준다)
a.update(국힙원탑='이지은') #a={'국힙원탑':'이지은','나의 아저씨':'이지안}

```