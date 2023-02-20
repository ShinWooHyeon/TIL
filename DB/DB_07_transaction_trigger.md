# Transaction
- 여러 쿼리문을 묶어서 하나의 작업처럼 처리하는 방법
- 쪼갤 수 없는 업무 단위 ,즉 모두 실패 or 모두 성공
- MY SQL은 기본적으로 자동 commit, 테이블을 Rollbak 했을 때와 commit 시
결과가 확연히 다르다
```sql
START TRANSACTION;

INSERT INTO singer(solo)
VALUE ('IU');
ROLLBACK;
COMMIT;
```

# Trigger
- 특정 이벤트에 대한 응답을 자동으로 실행하는 것
- 구문은 아래 코드와 같다
```sql
CREATE TRIGGER trigger_name
 BEFORE|AFTER  INSERT|UPDATE|DELETE -- 실행 전,후를 선택가능, DML 작업에만적용가능
 ON table_name FOR EACH ROW
 trigger_body; -- 트리거 활성화시 실행될 코드를 trigger body에 작성
 ```
 
 - trigger 코드 예시
 ```sql  
-- 게시글 수정시 필드값 업데이트하는 코드
 CREATE TABLE articles(
	id INT AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    createdAT DATETIME NOT NULL,
    updatedAT DATETIME NOT NULL,
    PRIMARY KEY(id)
);
SELECT * FROM articles;
INSERT INTO articles(title,createdAT,updatedAT)
VALUES ('title1',CURRENT_TIME(),CURRENT_TIME());
```

- DELIMITER는 여러개의 SQL문 작성시 종결기호를 변경하게 해준다
```sql
INSERT INTO articles(title,createdAT,updatedAT)
VALUES ('title1',CURRENT_TIME(),CURRENT_TIME());

DELIMITER // -- 여기서 부터 종료조건은 슬래쉬 2개가 종료조건이다 트리거문 묶어 주기 위해서 
CREATE TRIGGER myTrigger
	BEFORE UPDATE 
    ON ariticles FOR EACH ROW
BEGIN
	SET NEW.updatedAT=CURRENT_TIME();  -- 데이터 NEW OLD 결정가능
DELIMITER ;
```