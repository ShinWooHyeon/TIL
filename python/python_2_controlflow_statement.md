# 문자열,Data type 추가학습 
## 문자열 포맷팅
- `%`  fommating 
```python
'%s'%string
'%d'%number
'%f'%float
```
- `f`  formating
```python
name= '우현'
number='777'
f'{name} is {number}'
```
## 형 변환 (Typecasting)
- 암시적 형 변환 : 사용자 의도 x, 파이썬 내부적으로 형변환
``` python
True + 3 # 계산 결과 4
3 + 5.0 # 계산결과 8.0
```
- 명시적 형 변환 : 사용자가 특정 함수 이용, 의도적으로 자료형 변환

# 제어문
- 파이썬은 위에서 아래로 순차적으로 명령수행, 제어문은 특정 상황에 따라 선택적으로 실행하거나
  반복실행 할 수 있게 해줌
- 조건문과 반복문이 있다
## 조건문
- 참 거짓 판단할 수 있는 조건식과 함께 사용한다
- 조건이 참인 경우 if 이후 들여쓰기 되어있는 코드 실행, 이외의 경우 else 이후 코드 실행
```python
if <조건식>:
    <참인경우 실행되는 문장>
else:
    <이외의 경우 실행되는 문장>
```
- 복수 조건문 : elif를 활용하여 표현
```python
if <>:
    <>
elif <>:
    <>
elif <>:
    <>
else:
    <>
``` 
- 중첩 조건문: 조건문에 다른 조건문 중첩하여 사용
```python
if <>:
    if <>:

else:
    <>
```
# 반복문 -for
## Range
- 숫자 시퀀스 나타내기 위해 사용
- 범위 지정 range(m,n): m부터 n-1 까지 의 시퀀스
- 변경 불가(immutable) , 반복 가능(iterable)

## for
- for 문은 시퀀스(string ,tuple, list,range)를 포함한 순회 가능한(iterable) 요소 모두 순회
```python
for <변수명 > in <iterable>:
    #code 
```
- 문자열 순회
```python
# 방식 1
for char in chars:
    print(char)
# 방식 2, 추후 인덱스 까지 알 수 있다
for idx in range (len(chars)):
    print(chars[idx])
```
- 반복문 제어
    - break : 반복문 종료
    - continue 이후 코드 블록 수행 x, 다음 반복 수행
    - for-else: 끝까지 반복 실행후 이후 else문 실행 (break 통해 종료되면 else 문 실행 x)
**break 예시**
``` python
n= 0
while True:
    if n==3:
        break
    print(n)
    n+=1
# 0 1 2 출력되고 break 된다
```
**continue 예시**
```python
for i in range (6):
    if i% 2 == 0:
        continue
    print(i)
# 홀수만 출력하고 짝수는 continue 문 때매 출력x
```
**for- else문 예시**
```python
# break 안되고 끝까지 출력
for i in 'apple':
    if i == k:
        print("k가있다")
        break
else:
    print("k가 없네")
# break 되고 else문 실행 x
for i in 'snack':
    if i == k:
        print("k가있다")
        break
else:
    print("k가 없네")
```