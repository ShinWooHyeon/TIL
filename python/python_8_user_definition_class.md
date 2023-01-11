# 사용자 정의 클래스
## 객체 지향 프로그래밍
- 모든 것이 객체로 이루어진 파이썬
- 객체는 특정 타입의 `인스턴스(instance)`이다. ex) 1, 2, 3 모두 int의 인스턴스
- 객체의 특징: **타입**-어떤 연산자,조작?  ,**속성**-어떤 데이터?, **조작법**-어떤 함수(method)?
- 객체지향 프로그래밍:프로그램을 여러 개의 독립된 객체들간의 상호작용으로 파악하는 프로그래밍
- 객체지향 프로그래밍은 프로그램 유연하고 변경 용이하게 만들 수 있음, 직관적 코드 분석 가능
&nbsp;

<img width="357" alt="객체지향프로그래밍" src="https://user-images.githubusercontent.com/118239192/211739784-84a3b80e-e6b3-45c3-9cce-429656acd82d.png">

- 절차지향 프로그래밍과 달리 객체지향 프로그래밍은 데이터와 기능(메소드) 분리 가능,추상화 된 구조
```python

#절차 지향 프로그래밍
def area(x,y):
    return x*y

def cir(x,y):
    return 2*(x+y)
a=30 
b=20
c=40
d=10
area1=area(a,b)
area2=area(c,d)
cir1=cir(a,b)
cir2=cir(c,d)
# 객체 지향 프로그래밍
class Rectangle:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def area(self):
        return self.x*self.y
    
    def cir(slef):
        return 2* (self.x+self.y)

r1=Rectangle(30,20)
r1.area()
r1.cir()
r2=Rectangle(40,10)
r2.area()
r2.cir()    
```
위 사옹자 정의 클래스에서 **Rectangle은 클래스**, 각 사각형 **R1,R2는 인스턴스**, 사각형의 **가로길이 세로길이는 속성(attribute)**, 사각형의 **기능(넓이,둘레)은 메소드**이다

## 클래스와 인스턴스
- 객체의 틀(클래스,타입..)을 가지고 객체(인스턴스)를 생성, 즉 클래스는 객체들을 분류하는 타입, 모든 객체는 특정 타입(클래스)의 인스턴스이다 
- 속성: 특정 데이터타입,클래스의 객체들이 가지게 될 상태/데이터
- 메소드: 특정 데이터타입/클래스의 객체들에 공통적으로 적용 가능한 행위(함수,기능)
- 객체 비교시 `==`은 변수가 참조하는 객체가 동등한 내용일 경우 True, `is`는 동일한 객체 가르켜야 True

### 인스턴스
-인스턴스 메소드: 인스턴스 변수 사용하거나 ,인스턴스 변수에 값을 설정하는 메소드 ,호출시 첫 번째 인자로 인스턴스(객체) 자기 자신(self)가 전달된다
- **self**: 인스턴스 자기자신 , 호출 시 첫 번째 인자로 인스턴스 자신이 전달,매개변수 이름 self 암묵적 규칙
- 생성자 메소드: 인스턴스 객체가 생성될 때 자동으로 호출되는 메소드 `__init__`메소드 자동 호출
```python
class Person:
    def __init__(self):
        print("인스턴스 생성")
p1=Person() # "인스턴스 생성 출력 이렇게만 해도객체 호출하는 순간 __init__자동 호출되기 때문
```

- 소멸자 메소드 :인스턴스 객체가 파괴 전에 호출되는 메소드
```python
class Person:
    def __del__(self):
        print("인스턴스 삭제")
p1=Person()
del p1 # 인스턴스 삭제가 출력되고 p1이 사라진다 
```
- 매직 메소드 : Double Undersocre가 있는 메소드는 특수 동작 메소드
    - __ str__ : self 객체의이름을 바꿀 수 있다, 프린트 함수 호출시 자동 호출, 객체 출력형태 지정
    - __ gt__  : 부등호 연산자 사용시 호출된다
&nbsp;

<img width="398" alt="매직 메소드" src="https://user-images.githubusercontent.com/118239192/211744665-ab0991f1-25f5-4209-9679-e6c94f94d236.png">

위 코드를 보면 `p1>p2` 부등호 연산자가 사용됨에 따라 '__ gt__'가 사용되었다. 따라서 return self를 통해 객체 자신인 p1을 반환하는데 '__ str__'이 객체 자신 self의 출력 형태를 f'{self name {self age}' 형태로 하였기 때문에 마지막 두 줄 모두 self의 출력 형태가 변형되서 나온다
