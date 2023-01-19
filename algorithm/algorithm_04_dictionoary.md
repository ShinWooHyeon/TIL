# 딕셔너리 (Dictionary)
- 해시 테이블
    - 해시 함수: 임의의 길이 데이터를 고정 길이의 데이터로 매핑
    - 해시: 해시 함수 통해 얻어진 값
- 파이썬 딕셔너리의 특징
    - 삽입, 삭제, 수정 ,조회 `연산의 속도가 리스트보다 빠르다` (why?Hash Function으로 위치 바로 알 수 있다)
    - 딕셔너리 연산의 시간 복잡도 - 아래 4개 연산의 시간 복잡도는 모두 O(1) 이다 
        - Get Item
        - Update Item
        - Insert Item
        - Delete Item
        - Search Item
    - 즉 딕셔너리는 순서나 인덱스적 접근이 아닌 `데이터에 대한 빠른 접근` 시 효과적

- 딕셔너리와 리스트의 시간 복잡도 비교

<img width="589" alt="딕셔너리 리스트 시간복잡도" src="https://user-images.githubusercontent.com/118239192/213411241-aec53a7d-19d3-41e2-a40d-f112127fc821.png">

## 딕셔너리 기본 문법
- 기본 딕셔너리 사용법= `선언`
```python
a={'job':'singer','name':'IU'}
#key:value 형태로 직접 지정
```
- 딕셔너리 삽입 =  `딕셔너리[key]=value`
```python
a={}
a['job']='singer
# a={'job':'singer'}
```
- 딕셔너리 삭제 = 딕셔너리.pop(`key ,default`) = >키가 없으면 오류 defalut 설정하면 default 출력
- 딕셔너리 조회= 딕셔너리[key] ,딕셔너리.get(key,default)

## 딕셔너리 메소드
- .keys() : 딕셔너리의 key 목록 담긴 객체 반환
- .values(): 딕셔너리의 value 목록 담긴 객체 반환
- .items(): 딕셔너리의(key,value) 쌍 목록 담긴 객체 반환