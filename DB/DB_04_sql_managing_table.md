# Managing Tables
- 데이터(Table)의 기본 구조 및 형식을 변경할 수 있다
- Create,Delete ,Modiy를 통하여 테이블과 필드를 조작할 수 있다.

## Create Table
- 테이블을 생성하는 구문
- 구문은 `CREATE TABLE 테이블 이름 (컬럼명 데이터타입) ,constraints`
```sql
CREATE TABLE table_name(
    column_1 data_type,
    column_2 data_type
)
-- 위 코드를 통한 예시는 다음과 같다
CREATE TABLE posts(
	postid INT AUTO_INCREMENT ,
    title VARCHAR(50) NOT NULL,
    content VARCHAR(200) NOT NULL ,
    PRIMARY KEY(postid)
);
-- AUTO_INCREMENT(시작 값 1,자동으로 1씩 증가, NOT NULL 포함하는 제약조건)과 PRIMARY KEY(해당 필드를 기본 키로 지정), NOT NULL(필드에 NULL 값 저장 할 수없다) 제약 조건이 사용되었다 
```

## DELETE TABLE
- DROP TABLE 구문을 사용해서 테이블을 삭제한다 
- `DROP TABLE 테이블 이름`의 구문을 사용한다
```Sql
DROP TABLE
    userid;
```

## Modifying table fields
- ALTER TABLE 구문을 사용해서 테이블 내 필드를 변경한다
- 총 4가지 구문을 사용한다
    - ALTER TABLE `ADD` = 필드 추가
    - ALTER TABLE `MODIFY`= 필드의 속성 변경
    - ALTER TABLE `CHANGE COLUMN` = 필드 이름 변경
    - ALTER TABLE `DROP COLUMN`= 필드 삭제
```sql
-- ADD
ALTER TABLE 
	posts
ADD
	(writer VARCHAR(100) NULL DEFAULT 'Annoymous',
    created_at DATETIME NULL DEFAULT CURRENT_TIMESTAMP );
-- MODIFTY
ALTER TABLE
	posts
MODIFY
	content TEXT  NULL;
-- CHANGE COLUMN
ALTER TABLE
    posts
CHANGE COLUMN
    content newcontent VARCHAR(100) NULL ;
--원래 컬럼명 바꿀 컬럼명과 데이터 조건
-- DROP COLUMN
ALTER TABLE
	posts
DROP COLUMN
	writer;
```

