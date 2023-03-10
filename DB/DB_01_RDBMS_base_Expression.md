# 관계형 데이터베이스용어 정리
- 관계형 데이터베이스= 관계가 있는 데이터 항목들을 테이블,행,열 등으로 구조화 하는 방식
- 관계형 데이터베이스 주요 용어로 `Table`, `Field` , `Record`,`Database`,`Primary Key`,`Foreign Key`가 있다 
- Table
    - 데이터를 기록하는 곳, 하나의 작은 Data Set이라고도 할 수 있다.
    - 엑셀 시트같은 것이 대표적인 예시이다
- Field
    - 고유한 데이터 형식을 지정하는 곳
    - Column, Attribute라고도 한다. 데이터의 특징,속성이라고도 할 수 있다
    - 엑셀 시트의 한 열이 대표적인 예시이다
- Record
    - 구체적인 데이터 값이 저장되는 곳 
    - Row, Tuple이라고도 한다. 데이터의 모든 특징들을 기록하는 곳이라고 할 수 있다
    - 엑셀 시트의 한 행이 대표적인 예시이다
- Database
    - 테이블의 집합
    - Schema라고도 한다
    - 여러 시트(Table)이 모인 엑셀 파일이 대표적인 예시이다
- Primary Key (기본 키)
    - 각 Record의 고유한 값, 레코드의 식별자로 활용된다
    - 주로 id로 표현을 한다
    - 엑셀 테이블의 맨 처음 열의 번호 등이 대표적인 예시이다
- Foregin Key (외래 키)
    - Table의 `Filed` 중 다른 테이블의 레코드를 식별할 수 있는 키
    - 서로 다른 테이블간의 `관계`를 만드는데 사용
    - 엑셀시트에서 담당부서의 id가 Foregin key로 알려졌으면 , 그 key에 따라 이 레코드가 어느 Table에서 관리된느지 알 수 있다 