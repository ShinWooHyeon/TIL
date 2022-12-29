# 깃- Branch & Merge 정리

## Branch
- 독립적인 작업 흐름 만들고 관리할 수 있다.
![gitflow](https://techblog.woowahan.com/wp-content/uploads/img/2017-10-30/git-flow_overall_graph.png)

- 브랜치의 주요 명령어(`master`에서 )
```python
$ git branch <branch name> #branch 생성
```
```python
$ git chenckout <branch name> #branch 이동
```
```python
$ git checkout -b <branch name>  #branch 생성 및 이동
```
```python
$ git branch  #branch 목록
```
```python
$ git branch -d <branch name> #branch 삭제
```

## Merge
- 각 branch에서 작업한 이력 합칠때 `merge` 사용
- Merge 시 세 가지 경우 발생
    - 1.Master branch에서 `변경사항 x`
     => feature branch에서 commit , master branch에서 단순 merge
    
    - 2.Master branch와 feature branch `모두 변경 사항 O` + 변경 사항 다른경우
     => git에서 merge 알아서 해준다! (Merge made by the 'ort' strategy) , 
    
    - 3.Master branch와 feature branch `모두 변경 사항 O` + 변경 사항 겹칠경우
     => `merge conflict` 발생 , 버전이 만들어지지 않았다! status 확인 후 어떻게     수정해야할지 판단 !(수정 후 `add ,commit` 하면 git에서 커밋 메시지 추천해준다)

## Git Flow
- master(main): 배포가능한 상태의 코드
- develop(main): feature branch로 나눠지거나 개발 이후 release branch로 분기
- feature branch(supporting): 기능별 개발 branch
- release branch (supporting): 개발 완료 이후 , 배포 전 minor bug fix 등 반영
- hotfixes (supporting): 긴급하게 반영 해야하는 bug fix
-<h3 align='center'>   **정해진 Gitflow는 없다**

- Git flow의 기본 원칙
    - Master branch는 배포 가능한 상태
    - feature branch는 기능 알도록 작성
    - Commit message는 명확하게 작성
    - Pull request 통해 협업
    - 변경사항 반영은 master branch에

## 협업 모델
### Shared Repository Model
- 팀원 등록, 저장소에 push 권한 부여
- 브랜치에서 작업 후 github에 push => github에서 Pull request 생성 => Review,merge
- 다시 작업하고 싶을 경우 pull 후 local에서 작업

### Fork &Pull Request Model
- 원격 저장소를 Fork, 내 저장소로 복제본 가져온 후 push 가능
- 이후 작업은 위와 동일 (커밋 , push, PR)
