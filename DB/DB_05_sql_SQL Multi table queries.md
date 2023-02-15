# Join 
- 관계형데이터베이스= 데이터들간의 관계 有
- 테이블을 분리해서 관리해야 기능용이 , 이 경우 `테이블간 연결`해 데이터 확인 가능
- 이 연결을 하는 것이 `Join`이다

## Joining Tables
- Join Clause: `둘 이상의 테이블`에서 데이터 검색, 연결하는 방법
- INNER JOIN/  RIGHT JOIN,LEFT JOIN이 있다.
- INNER JOIN 
    - 두 테이블에서 값이 일치하는 레코드에 대해서만 결과 반환
    - SELECT <select_list> FROM <table_1> INNER JOIN <table_2> ON 조건
    - FROM절 이후 메인 Table,INNER JOIN 이후 조인 할 테이블 ON 이후 Join 조건 작성
- LEFT JOIN 
    - 왼쪽테이블의 모든 레코드와 왼쪽 테이블의 레코드와 일치하는 오른쪽 테이블의 레코드 반환
    - SELECT <select_list> FROM <table_1> LEFT JOIN <table_2> ON 조건
- RIGHT JOIN
    - 오른쪽 테이블의 모든 레코드와 함꼐  오른쪽 테이블의 레코드와 일치하는 왼쪽 테이블의 레코드 반환
    - SELECT <select_list> FROM <table_1> RIGHT JOIN <table_2> ON 조건

```sql
-- LEFT JOIN 
SELECT customerNumber,officeCode, customers.city ,offices.city
FROM customers
LEFT JOIN	offices
	ON customers.city=offices.city
ORDER BY
	customerNumber DESC;
    
-- RIGHT JOIN
SELECT customerNumber,officeCode, customers.city ,offices.city
FROM customers
RIGHT JOIN	offices
	ON customers.city=offices.city
ORDER BY
	customerNumber DESC;

-- INNER JOIN
SELECT customerNumber,officeCode, customers.city ,offices.city
FROM customers
INNER JOIN	offices
	ON customers.city=offices.city
ORDER BY
	customerNumber DESC; 
```
## JOIN 정리
![image](https://user-images.githubusercontent.com/118239192/218998485-bcacef8c-80dc-40a9-a1d5-07322df7af5b.png)
