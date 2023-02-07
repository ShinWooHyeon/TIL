# 구현 (Implementation)
- 문제 제시 과정을 그대로 구현하는 것
- 시뮬레이션 예시
```py 
# BOJ 1063번
move={'R':(0,1),'L':(0,-1),'B':(1,0),'T':(-1,0),'RT':(-1,1),'LT':(-1,-1),'RB':(1,1),'LB':(1,-1)}
width='ABCDEFGH'
k,s,N=input().strip().split()
k_place=(8-int(k[1]),width.index(k[0]))
s_place=(8-int(s[1]),width.index(s[0]))
# 문자를 좌표로 좌표를 다시 문자로 바꿔주고, 이동하는 방향을 튜플로 만들어서 해결한다
```

- 완전탐색 예시 (BOJ 4963번): DFS 알고리즘을 재귀함수를 이용하여 계속 찾는다 
(추가 공부 필요)

