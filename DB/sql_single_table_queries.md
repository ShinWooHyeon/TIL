# SQL
- SQL= `Structure Query Language`, 테이블 형태로 구조화된 데이터 정보 저장,처리위한 프로그래밍 언어이다
- SQL Syntax등을 통하여 데이터베이스를 다룰 수 있다.
- SQL Syntax 는 대소문자 상관 없지만, 관용적으로 `대문자` 권장, 끝에는 `세미콜론(;` 필요

## SQL Statements
- 데이터 베이스에서 수행 목적에 따라 4가지로 나뉘어진다
    - DDL-데이터 정의
    - DQL-데이터 검색
    - DML- 데이터 조작
    - DCL- 데이터 제어
- SQL Statements의 유형
![image](https://user-images.githubusercontent.com/118239192/217782962-99432602-515a-496d-ac1b-9ee22fd778fa.png)


## SQL Single Table Queries
1. Querying Data
- SELECT Syntax를 통하여 데이터를 조회할 수 있다.
```sql
SELECT selectlist FROM tablename
```
- 여러개 조회를 원할경우 콤마 통해서 조회가능
- `AS` 키워드 이용하여 조회시 원하는 이름으로 출력가능
```sql
SELECT selectlist AS IU FROM tablename
```
- SELECT *(asterlisk)로 모든 필드 선택도 가능하다
- SELECT 내에서 사칙연산 역시 가능하다
```sql
SELECT num*price AS '가격' FROM tablename
```