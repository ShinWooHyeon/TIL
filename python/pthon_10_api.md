# 가상환경 (수업 진행은 x)
- 프로젝트 마다 사용 버전 다를 수 있다 => 가상환경 만들어 프로젝트 별 패키지 활용 가능
- **venv** : 가상환경 만들고 관리하는데 사용되는 모듈
    - 특정 디렉토리에 가상환경 만들고 고유한 파이썬 패키지 집합 생성 가능
    - $ python -m venv <폴더명> 으로 가상환경 생성 가능

# 외부 패키지 활용 (requests)
- 파이썬을 통해 주소로 요청 보내고 응답 결과 파이썬으로 조작 가능
- Requests: 파이썬의 Simple한 HTTP 라이브러리

## API
- Application Programming Interface:
    - 컴퓨터나 컴퓨터 프로그램 사이의 연결
    - 일종의 소프트웨어 인터페이스이며 다른 종류의 소프트웨어에 서비스를 제공한다
- API 활용시 유의사항
    - 인증 방식 
    - URL 생성 (기본 URL과 추가 경로)
    - 응답 결과에 대한 이해

API 활용 예시
```python
import requests
def search_movie(title):
    base_url='https://api.themoviedb.org/3' #Base Url 경로들 이 기본 url에 추가하면서 정보 확인가능
    query=title
    path='/search/movie'
    params={'api_key':'57f3a6beace950c5f2cbf25a6bb1eb0a','language':'ko','query' :query} #자동 Parmas로 URL 변환 코드
    response=requests.get(base_url+path,params=params).json() # 파일 형식 고려, request 요청하고 응답 받아온다
```

