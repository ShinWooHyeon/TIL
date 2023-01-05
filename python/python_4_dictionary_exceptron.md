# 컬렉션 
## 딕셔너리
- key, value 형태로 이뤄진 모음
    - key: 불변 자료형만 가능 (리스트, 딕셔너리 등은 x)
    - value: 어떤 형태든 관계 x
- key와 value는 :로 구분, 개별 요소는 ,로 구분
- `변경 가능(mutable)`하다 (반복도 가능, 반복 시 키가 반환된다.)
- 딕셔너리에 키와 값의 쌍 추가 가능, 이미 해당키 있으면 기존 값 변경
```python
a={'1':'아이유','2':'이지은','3':'이지금'}
a['4']='이지동'
print(a) #{'1': '아이유', '2': '이지은', '3': '이지금', '4': '이지동'}

b={'1':'장만월','2':'이지안','3':'해수'}
b['3']='신디'
print(b) #b={'1':'장만월','2':'이지안','3':'신디'}
```

- 추가 매서드
    - keys(): key로 구성된 결과
    - values(): value로 구성된 결과
    - items() : (Key,Value)의 튜플로 구성된 결과

## 모듈, 패키지, 라이브러리
- 모듈 = 다양한 기능을 하나의 파일로 만든 것(py)
- 패키지 = 다양한 파일을 하나의 폴더로 , 여러 모듈의 집합이다. 패키지 안에 또 다른 서브 패키지를 포함한다
- 라이브러리 = 다양한 패키지를 하나의 묶음으로 만든 것

### 파이썬 표준 라이브러리 (PSL)
- 파이썬에 기본적으로 설치된 모듈과 내장함수
- random : 숫자/수학 모듈 중 의사 난수 생성
    - random.randint(a,b): a이상 b이하의 임의의 정수 N 반환
    - random.choice(seq): 비어있지 않은 시퀀스에서 임의요소반환
    - random.shuffle(seq): 시퀀스를 섞는다
    - random.sample(population,k): k개를 무작위 비복원 추출 리스트 반환
- datetime : 날짜와 시간 조작하는 객체 제공
    - datetime.date(year, month, day) :모든 인자 필수, 특정범위안에 있어야함 범위 벗어나면 Value Error
    - datetime.date.today():현재지역 날짜 반환
    - datetime.datetime.today():현재 지역 datetime 반환
- OS : 운영체제 조작위한 인터페이스 제공
    - os.listdir(path=''): path에 있는 항목 리스트 반환
    - os.mkdir(path): path라는 디렉토리 만든다
    - os.chdir(path): path 변경

### 파이썬 패키지
- pip 로 설치 
```python
$ pip install Somepackage
$ pip install Somepacakge =1.0.5 #버전까지 고려해서 설치가능
```
- 일반적으로 패키지 기록 파일 requirements.txt로 정의, 아래처럼 설치 가능
```python
$ pip install -r requirements.txt #여러 패키지 미리 txt에 다기록, 한번에 설치가능
```

## 에러/예외처리
- 에러는 제어가 되는 시점(조건/반복, 함수)에서 `값이 변경되는시점`에서 자주 발생한다
- branches :모든 조건이 동작하는가
- for loops: 반복문에 진입하는지, 원하는 만큼 실행되는지
- while llops: 종료조건 동작하는가?
- function : 함수결과, 함수 파라미터 등등..
### 에러
- Syntax Error(문법 에러) : 파이썬 실행 x, 파일이름,줄번호,^ 문자 통해 문제 발생위치 표현
    - EOL: End of Line
    - EOF: End of file
    - Invaild Syntax
    - assign to literal
### 예외
- 실행 도중 예상치 못한 상황 발생, 실행 멈춘다
- `실행 중에 감지되는 에러` 가 예외이다.
    - ZeroDivisionError , NameError, TypeError, ValueError, Index Error, KeyError,ModuleNotFoundError , ImportError ,IndentationError ..

## 예외처리
- try / except 절 이용해서 예외 처리가능하다
- try문: 오류 발생 가능한 코드 실행, 예외 발생 안하면 excpet없이 종료
- except 문: 예외 발생시 except 절 실행, 예외처리코드 받아 실행

- try 문은 반드시 한개 이상의 except 구문 필요

- 코드예시

<img width="428" alt="예외처리 코드" src="https://user-images.githubusercontent.com/118239192/210742914-d8c909de-0da2-474a-8cd7-b0f1d6c0a193.png">

- 에러 별로 except 구문을 넣어 복수의 예외처리도 가능하다 
- 정리하자면 
    - try문: 코드 실행
    - except: try문에서 예외 발생시 실행
    - else : try문에서 예외 발생 안하면 실행
    - finally : 예외 발생 여부와 관계없이 항상 실행

# 예외 발생 시키기
- `raise` 통해 강제로 발생 시킬 수 있다, 실제 플덕션 코드에 활용

```python
raise <표현식>(메시지)
#표현식은 예외타입을 지정하는 것,주어지지 않으면 현재 스코프에서 활성화된 마지막 예외 발생시킴
```

- assert 를 통해서도 강제로 예외 발생 가능 , assert는 디버깅 용도에 자주 사용(표현식이 False인경우 AssertionError발생)

```python
assert <표현식>. (메시지)
```
