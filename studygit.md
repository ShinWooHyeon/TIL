# Git 정리
## Git 이란?
- Git은 분산 버전 관리 시스템을 의미한다.
- Git의 가장 큰 특징은 `로컬` 에서도 버전 관리가 가능하다는 것이다!!

## Git의 사용 방법
- 작업을 한다 => 변경된 파일들을 추가해 => 버전을 만든다
    - 용어정리
        - change,working => ` Add` => `Commit`
        - Working directory => Staging area => Head
## Git의 파일들의 상태 
- `Modified` = 파일이 수정되었지만 'Add' 되지 않아 커밋이 불가한 상태
- `Staged`   = 수정한 파일이 'Add' 된 후 커밋되기 전 상태 (커밋이 가능한 상태) 
- `Committed` = 커밋이 된 상태

## Git의 명령어 정리
```python
<init>
$ git init #저장소 처음 만들때
```

``` python
<Add>
$ git add <file> #Staged 상태로 변경 , 커밋이  가능
```
``` python
<Commit>
$ git commit -m '커밋메시지' #커밋, 즉 버전을 기록
```
``` python
<Status>
$ git status  #파일의 상태를 알 수 있다
`Unmodified` , `Modified` ,`Staged` , `Untracked` 확인가능 
```

``` python
<Log>
$ git log # 현재 저장소에 기록된 커밋 조회 가능
```
