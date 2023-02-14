# Single talbe queries
## Filtering Data
- Clause
    - Distinct Clause: 조회결과에서 중복된 레코드를 제거해준다
    - Where Clause: 조회 시 특정 검색 조건을 지정해준다
    - Operator :조건 설정 시 사용
        - Comaprison Operator (비교 연산자): 부등호, IS,LIKE,IN,BETWEEN..AND
            - Like Operator는 값이 특정 패턴과 일치하는지 확인하는 wild card이다
        - Logical Operator (논리 연산자):AND , OR , NOT
    - Limit Clause: 조회하는 레코드 수를 제한한다
        - OFFSET 사용시 건너 뛰고 조회가능  


```sql 
-- Distinct 예시
SELECT DISTINCT country FROM customers ORDER BY country;

-- Where 예시
-- Like 사용
SELECT  customerNumber , customerName , phone  FROM customers WHERE phone Like'%555' ORDER BY customerName DESC;

-- Logical Operator 사용
SELECT productCode , productName , quantityInStock  FROM products WHERE quantityInStock BETWEEN 2000 and 3000 ORDER BY quantityInStock DESC;
-- Limit Clause
SELECT  productCode , quantityInStock FROM products ORDER BY quantityInStock DESC LIMIT 5;
```

## Grouping Data
- GROUP BY CLAUSE: 레코드를 그룹화하여 요약본을 생성한다
    - FROM ,WHERE 절 뒤에 배치한다
    - GROUP BY 절 뒤에 필드화 할 필드목록을 작성한다
    - GROUP BY 그룹 중 조건이 있다면 HAVING을 통하여 설정한다
```sql
-- GROUP BY Clause
SELECT productline,max(quantityInStock) as max_stock FROM products GROUP BY productline HAVING max_stock<9000 ;
```

## SELECT STATEMENT 순서 정리   
![image](https://user-images.githubusercontent.com/118239192/218480761-52b4688e-58cd-46bc-a821-df2ceae4dea8.png)

