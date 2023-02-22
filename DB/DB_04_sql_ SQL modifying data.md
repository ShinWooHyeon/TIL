# Modifting Data
- 테이블 새로운 정보를 추가하거나 기존 레코드 수정할 수 있다
- Insert ,Update, Delte 할 수 있다

## Insert Data
- 테이블에 레코드를 삽입하는 구문, 
- `Insert 테이블명(필드목록) VALUES (삽입할 값 목록)` 의 구문형태

## Update Data
- 테이블의 레코드를 수정하는 구문
- `Update talbe_name SET column_name=expression <WHERE구문추가가능>`
## Delete Data
- 테이블의 레코드를 삭제하는 구문
- `Delete FROM table_name <WHERE 구문 추가 가능>`

```sql
--insert Data
INSERT INTO 
	users(first_name,last_name,birthday,city,country,email)
VALUES
	('Modern-Times', '3', '2013-01-08', 'Seoul','Korea', NULL),
    ('Chat-shire', 'Mini', '2015-10-23','Seoul','Korea',NULL),
    ('Pallete', '4', '2017-04-21', 'Seoul','Korea', NULL),
    ('Lovepoem', 'Mini','2019-11-18', 'Seoul','Korea',NULL),
    ('Lilac','5','2021-03-25','Seoul','Korea',NULL);

-- Update Data
UPDATE 
	users
SET
	first_name='WooHyeon',
    last_name='Shin',
	birthday='1998-01-09'
WHERE
	userid=2;_
-- Delete Data
DELETE FROM 
	users
WHERE
	first_name= 'Beemo';
```_