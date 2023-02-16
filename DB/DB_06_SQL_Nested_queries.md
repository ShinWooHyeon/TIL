# Subquery
- 단일 쿼리문에 여러 테이블의 데이터를 결합하는 방법
- 하나 이상의 테이블에서 데이터를 검색하는데 사용된다
```sql
SELECT MAX(amount) FROM payments;
-- 위 쿼리를 이용해서 payment 최대인 customerNumber 찾고싶다 
SELECT customerNumber, amount 
FROM payments 
WHERE amount=(SELECT MAX(amount) FROM payments);
-- 
SELECT 
	cs.customerNumber,customerName,order_count
FROM
	customers AS cs
INNER JOIN
	(SELECT 
	customerNumber,count(*) AS order_count 
FROM 
	orders
GROUP BY
	customerNumber 
ORDER BY order_count DESC
LIMIT 1)AS os
ON 
	cs.customerNumber=os.customerNumber;
-- Join, Group 과 함께 쓰일 수도 있다.
```

## Exist syntax
- subquery가 하나 이상의 행을 반환하면 EXIST 연산자는 TRUE,그렇지 않으면 False 반환
- WHERE 절에서 자주 사용된다
``` sql
SELECT select_list
FROM table_name
WHERE
    EXIST (SELECT ~) -- subquery
```

## Conditional Statements
- Case statement를 이용하여 조건문을 구성한다
```SQL
SELECT __,__
    CASE case_value
        WHEN when_value1 THEN statement_1
        WHEN when_value2 THEN statement_2
-- 조건에 따라 데이터 확인할 때 사용한다
```