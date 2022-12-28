# (Do it!) 깃&깃허브 입문 : 지옥에서 온 문서 관리자

# 1장 깃 시작하기
- 깃의 환경설정 
```python
$ git config --global user.name "이름"
$ git config --global user.email "메일 주소"
``` 
- 리눅스 명령어 연습
``` python
$ pwd  "현재 위치의 경로"
$ ls   "현재 디렉터리의 파일 리스트"
$ ls -l"현재 디렉터리의 파일 리스트+상세정보"
$ clear "터미널창 지우기"
```
```python
$ cd .. "상위 디렉토리 이동"
% cd <하위디렉토리> " 하위 디렉토리 이동"
$ mkdir <디렉토리명> "디렉토리 생성"
$ rm -r <디레고리명> "디렉토리 삭제"
```

## 2장 깃으로 버전 관리하기 

- 저장소를 만들기 위해서는 다음과 같은 코드 입력
``` python
$ git init 
```
- 스테이지와 커밋 이해하기
    - 작업트리 = 파일 수정,저장 등 작업하는 디렉토리
    - 스테이지 = 버전으로 만들 파일 대기하는 곳
    - 저장소 = 스테이지에 있던 파일 버전으로 만들어 저장하는 곳

- 수정한 파일을 스테이지에 올리기 `<Add>`
```python
$ git add <파일명>
```
- 스테이징한 파일 커밋하기 `<commit>`
```python
$ git commit -m`커밋메시지` 
```
- 깃의 상태 확인 `<status>`
```python
$ git status
```
- 깃의 버전(커밋기록) 확인 `<log>`
```python
$ git log
```
- 수정한 파일의 스테이징,커밋 동시에 처리 `<commit -am>`
```python
$ git commit -am<커밋메시지>
```
- 수정한 파일이 저장소에 있는 최신 버전과 어떻게 다른지 확인
```python
$ git diff 
```
- 저장소 내 파일들의 상태
    - tracked: 버전을 한 번이라도 만들었던 파일
    - unmodified : 아무런 변경 사항 없는 파일
    - modified: 파일이 수정만 된 상태(Changes not stage for commit)
    - staged : 커밋 직전 단계 (Changes to be committed)
