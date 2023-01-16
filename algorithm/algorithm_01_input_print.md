# 알고리즘이란?
- 알고리즘: 어떤 문제를 해결하기 위한 일련의 절차나 행동 , Input 넣었을 때 원하는 Output 나오게 한다.

## 데이터 구조와 알고리즘
- 프로그램은 데이터 구조와 알고리즘으로 이루어진다
- 데이터 구조는 데이터를 다양한 방식으로 저장하고, 조회 삽입 변경 등 조작 기능을 제공한다
- 데이터 구조는 문제 해결을 효율적으로 풀기 위한 도구가 된다.
- 파이썬의 기본 데이터 구조 (컨테이너)
    - 시퀀스형 
        - 리스트, 튜플, 레인지
    - 비시퀀스형
        - 세트, 딕셔너리
## **문제 해결을 위한 데이터 구조와 알고리즘**
    - 데이터 구조
        - Array(배열)
        - Linked List(연결 리스트)
        - Hash (해시)
        - Stack (스택)
        - Queue (큐)
        - Priority Queue(우선순위 큐)
        - Heap (힙)
        - Tree (트리)
        - Grph (그래프)
    - 알고리즘
        - 기본
            - 완전탐색 알고리즘
            - 재귀 알고리즘
            - 시뮬레이션
            - 그리디
        - 심화
            - DFS
            - BFS
            - 백트래킹
            - 이진탐색
            - DP
            - 다익스트라
            - 크루스칼
            - 프림

# 입력과 출력
- `input()`과 `print()`를 활용하여 다양하게 입출력이 가능하다
```python
a,b,c=map(int,input().split())
print(a+b+c)  # 1 2 3 이면 6

a='IU'
b='dlwlrma'
print(a,b)
#IU dlwlrma
print(a,end='@')
print(b)
#IU@dlwlrma
print(a,b,sep='\n')
#IU
#dlwlrma
print(a,b,end='@')
#IU dlwlrma@
```