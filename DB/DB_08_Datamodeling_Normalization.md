# Normalization (정규화)
- RDB 설계 중 중복 최소화 하며 DB를 설계하는 과정 
- 데이터의 효율적, 편리한 관리를 위해 진행한다 
- 제1 정규화~ 제3정규화 까지 진행한다

- 제 1 정규화
    - 데이터 베이스 각 필드는 `하나의 값`만 저장한다 
        - 예시) 주문상품이 여러개인 필드 => 각 상품별로 주문을 나눈다
        - 반복되는 부분을 찾아 키 값으로 설정, 필드를 생성한다  
        - (위 예시를 따를 경우 주문상품은 다르지만 주문자와 날짜가 유사한 정보 중복)
        
    - 유사한 정보를 저장하는 두 개의 필드가 있어서는 안된다
        - 주문자와 날짜가 유사하다 => 주문정보라는 KEY로 묶고 새로운 테이블을 생성한다

- 제 2 정규화
    - KEY 값을 통해서 데이터 특정 지을 수 있을 경우 테이블을 분할한다
        - 에시) 판매개수에 상품코드-상품명-상품개수 , 상품코드-상품개수와  상품코드-상품명으로 분할한다
    
- 제 3 정규화
    - 마지막으로 기본 키 이외의 부분에서 중복을 조사한다.


# Data Modeling
- 데이터베이스 시스템을 시각적으로 표현하는 과정
- ER Diagram(Entity-Relationship) 을 사용하여 데이터베이스 entity간 관계 표현 가능

## ER Diagram
- 구성요소 : Entity(Table), Attribute(Field), Relation(PK,FK)
- Entity를 정의=> Attribute 정의 => Relationship 정의
- Cardinality (1|N) , Optionality (Mandatory|Optional)  =>기수와 선택가능성 표현가능
    - 1:1 관계 = 직선
    - 1:N 관계 = N으로 받는 Entitry에게 Crow Foot 표시
    - M:N 관계 = 두 Entity 모두에게 Crow Foot 표시
    - 어떤 Entity가 있으려면 반드시 존재해야하는 Entity: Mandatory `|` 표시, 선택적이면 `O` 표시
- 예시 EDR
![image](https://user-images.githubusercontent.com/118239192/220315503-ae4f0fbb-0dff-4c02-b9cd-428455ff5b70.png)
