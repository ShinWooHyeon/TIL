# 사용자 정의 함수
- 함수의 기본 구조: 선언과 호출 (defintion&call),입력(input),범위(scope),output(결과)
- 선언과 호출  
    - def 키워드를  활용한다
    - 들여쓰기 후 function block 작성
    - 함수는 parameter 넘겨 줄 수 있으며, `return` 통해 결과값 반환
``` python
def iu():
    return True
def dlwlrma(x,y):
    return x + y  #파라미터 있는경우 호출 시 함수명(값1,값2...)로 호출해야함
```
- 함수의 결과값
    - 함수는 반드시 값을 하나만 return 한다 (명시적인 Return 없으면 None 반환)
    - 함수 Return과 동시에 실행종료
    - return 은 함수 안에서 값 반환하기 위해 사용, print는 출력 
```python
def aa(a,b):
    return a+b 
    return a-b  # 실행 x, return문이 2개니까 한번에 2개 이상의 값 return 원하면

def aa(a,b):
    return a+b, a-b # (a+b, a-b) 형태의 튜플값으로 반환할 수 있다. 
```
- 함수의 입력
    - Parameter: 함수를 실행할 때 함수 내부에서 사용되는 식별자
    - Argument: 함수를 호출할 때 넣어주는 값 (함수 호출시 함수의 parameter를 통해 전달되는 값 )
        - 필수 Argument: 반드시 전달되어야 하는 argument
        - 선택 Argument: 값을 전달하지 않아도 기본 값이 전달된다.
        - Argument 특징
            - 함수 호출시 Argument는 위치에 따라 함수에 전달된다 ( def(x,y)에서 def(1,2)면 함수 내 x=1, y=2)
            - 직접 변수의 이름으로 특정 argument 전달 가능 (def(x,y)에서 def(x=1,y=2) 또는 def(2,y=2) 등 활용)
            - Default Argument Value,즉 기본값 설정 가능 ( def(x,y=2)면 def(2)면 y에 2 알아서 기본지정)
        - Argument의 개수를 정하지 않고 받을경우
            - Argument들을 튜플로 묶어 처리, parameter에 * 붙여표현
        - Keyword Argument의 개수를 정하지 않고 호출할 경우
            - Argument들은 딕셔너리로 묶어서 처리,parameter에 ** 붙여서 표현
```python
# Argument의 개수를 정하지 않았을 때
def add(*args):
    for arg in args:
        print(arg)   #add(2),add(2,3,4) 등 여러개 받을 수 있다.

# Keyword Argument의 개수를 정하지 않았을 때 
def family(**kwargs):
    for key ,value in kwargs:
        print(key,":",vaule)
family(father='john',mother='hanna')
```

- 함수의 범위 (scope)  
    - 함수는 코드 내부에 `local scope` 생성 그 외 공간을 global scope
    - scope에는 코드 어디에서든 참조 가능한 global scope, 함수내에서만 참조 가능한 local scope 가 있다
    - variable에는 global scope에서 정의된 global variable, local scope에서 정의된 local variable이 있다.
    - 객체수명주기
        - built in scope (파이썬 실행 이후 영원히 유지).. 내장함수 같은 것들 
        - global scope(모듈 호출 이후 혹은 인터프리터 끝날 때까지)
        - local scope(함수 호출 때 생성, 함수 종료될 때까지 유지)
        - global 문 : 현재 코드 블록 전체에 적용되며, 나열된 variable이 global variable임을 나타낸다.
```python
def iu():
    a=30
    print(a)
iu()
print(a) #맨 마지막 문장 오류 a는 local scope에서만 존재한다
```
```python
a=5
def iu():
    print(a) # 로컬 scope에는 a가 없는데? 이후 global scope에서 a 찾아서 사용
def iiu():
    a=3
    print(a)
iu()  # 5로 출력
iiu() # 3으로 출력, 로컬 scope에서 a 먼저 찾아서 사용
```
```python
a=5
def iu():
    global a
    a=3
print(a) # global scope에서 정의된 a=5 그대로 출력된다
iu() # 함수가 사용된 후 a는 global variable이며 3으로 정의되었다.
print(a) # 3으로 출력
```
- 이름 검색 규칙 (LEGB Rule)
<img width="522" alt="LEGBRULE" src="https://user-images.githubusercontent.com/118239192/211473650-93f025e7-1978-4745-8596-9c3863a9ad35.png">
