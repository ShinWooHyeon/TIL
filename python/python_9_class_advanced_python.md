# 클래스
- 클래스 속성 
    - 한 클래스내의 모든 인스턴스라도 똑같은 값 가지는 속성,
    - 클래스 선언 내부에서 정의된다.
    - <classname>.name으로 할당한다

- 클래스 메소드 
    - 클래스가 사용할 메소드    
    - @classmethod 데코레이터 사용해서 정의
    - 호출 시 첫 번째 인자로 클래스(cls)전달

- 스태틱 메소드
    - 인스턴스나 클래스 사용하지 않는 메소드
    - @staticmethod 데코레이터 사용 정의
    - 호출 시 어떠한 인자도 전달되지 않음
 

- 메소드 정리
    - 인스턴스나 클래스 활용하지 않고 조작도 안한다 => `스태틱 메소드`
    - 인스턴스를 활용하거나 조작하는 경우 => `인스턴스 메소드` 첫 번째 인자로 전잘된 인스턴스 조작(`self`)
    - 클래스를 활용하거 조작=> `클래스 메소드` 첫 번째 인자로 전달된 클래스 조작(`cls`)

```python
class IU:
    def method(self):
        return 'instance method', self
    @classmethod
    def classmethod(cls):
        return 'class method', cls
    @staticmethod
    def staticmethod():
        return 'static method'
```
- 인스턴스 자체에 속성이 없는 경우는 클래스에 있는 것을 가져다 쓸 수 있다
- 인스턴스 별 이름공간을 먼저 확인한 후 없을 경우 클래스 이름 공간에 속성을 확인한다

# 클래스 상속
- 부모에 정의된 속성이나 메서드를 활용하거나 오버라이딩(재정의)을 통해 활용한다 
- super() 자식클래스에서 부모 클래스 사용하고 싶은 경우 활용
- 메서드 재사용
&nbsp;


<img width="500" alt="메서드 재사용" src="https://user-images.githubusercontent.com/118239192/211998556-9f25218e-de96-44d9-b976-afd9b8071fad.png">

- 메서드 오버라이딩 = 상속받은 메소드를 재정의(상속받은 클래스에서 같은 이름의 메소드로 덮어씀)
```python
class Dlwlrma:
    def singer(self,name):
        self.name=name
    def hi(self):
        print('하이하이')
class IU(Dlwlrma):
    def hi(self):
        print('반갑습니다')  # 이렇게 변경시켜서활용 가능하다

```

## 다중상속
```python
# Class IU ,Class Dlwlrma, Class Star 있다치면
class IU:
    a=1

class Dlwlrma:
    b=2

class Star(IU,Dlwlrma): # 이런 형태로 상속 가능 
```

# 파이썬 심화
```python
value= num if num>=0 else -num  # 한 문장안에 if else문 넣어서 표현 가능하다
# 위 코드는 아래코드와 동일
if num>=0:
    value=num
else:
    value=-num
```
- enumerate (): 인덱스와 객체를 쌍으로 담은 열거형 객체 반환(index,value)
- List Comprehension: 리스트 안에 for문이나 if문 넣어서 리스트 생성 가능 
```python
a=[2**i for i in range(1,4)] # 2의 거듭제곱 리스트
```
- Dictionary Comprehension: 딕셔너리 안에 for문이나 if문 넣어서 생성가능
```python
a={number:number**3 for number in range(1,4)}
```
- Lambda 표현식: 표현식을 게산한 결과값을 반환하는 함수 (함수의 이름이 없다), 함수를 간결하게 사용가능
    - return문을 가질 수 없다
    - 간편 조건문 이외의 조건문,반복문 가질 수 없다
    - lambda [parameter]:표현식 의 형태
```python
num=[3,6]
print(list(map(lambda n:n//2,num))) #n을 numbers에서 받을건데 2로 나눈 몫으로 반환할것이다
```

## 파이썬 버젼별 차이
- Type Annotation:파이썬 작성시 각 타입에서 코드 작성 방식에 대한 도움을 받을 수 있음
- Positional- Only parameters: 함수를 정의할 때 어떻게 호출해야하는지를 지정
<img width="525" alt="positional-only" src="https://user-images.githubusercontent.com/118239192/212003724-250fa4cd-2b49-403a-8fda-ef3bb6d5bdd5.png">

- `/` 전까지 위치로만 받을 수 있고, `\` 이후부터  `*`까지는 위치와 키워드 모두, `* `이후는 키워드만 작성이 가능하다