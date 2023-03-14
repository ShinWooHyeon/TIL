# Syntax of Javascript
1. 식별자(변수명)
- 문자,밑줄,달러($)로 시작해야 한다.
- `대소문자 구분`, 클래스 제외 모두 소문자로 시작
- 예약어 (for,if 등) 사용 불가
- 종류
    - 카멜 케이스 (camelCase) - 변수,객체,함수에 사용 `소문자 시작,중간 대문자`
    - 파스칼 케이스 (PascalCase) - 클래스, 생성자에 사용 `대문자 시작, 중가 대문자`
    - 대문자 스네이크 케이스 (SNAKE_CASE) - 상수에 사용 
- 변수 선언 키워드 (const 사용 권장,재할당 해야할 시 let 사용)
    - let : 블록 스코프 갖는 지역변수 선언 `재할당 가능, 재선언 불가`
    - const : 블록 스코프 갖는 지역변수 선언 `재할당 불가, 재선언 불가`
- 블록 스코프(Blcok Scope) : if ,for 함수 등의 `중괄호 내부` 가리킴 (블록 바깥에서 접근 불가)
```html
<script>
    let x=1
    if (x===1){
        let x=2
        console.log(x) //2
    }
    console.log(x) //1
</script>
```

2. 데이터 타입 
- 원시 자료형 : Number, String, Boolean ,undefined ,null => 변수에 값이 직접 저장 (불변, 값이 복사)
- 참조 자료형 : Objects (Object,Array,Function) => `객체의 주소`가 저장 (가변, 주소가 복사)
```html
<script>
// 원시 자료형
const bar='iu'
console.log(bar) //iu
bar.toupperCase()
console.log(bar) //iu

let a=10
let b=a
b=20
console.log(b) //20
console.log(a) //10

// 참조 자료형
const obj1={name:'iu',age:30}
const obj2=obj1
obj2.age=40
console.log(obj1.age)//40
console.log(obj2.age)//40
</script>
```
- 데이터 타입
    - Number : 정수 또는 실수형 숫자를 표현
    - String : 텍스트 데이터 자료형 (곱셉, 나눗셈, 뺄셈은 안되지만 `덧셈`은 가능)
    - Template-literal: 파이썬 f 포맷팅 처럼 문자열 사이에 변수 삽입 가능 `$`와 `중괄호{}` ,`(백틱) 사용
    - nulll :변수의 값이 없음을 의도적으로 표현 / undefined: 변수 선언 이후 값 할당하지 않을경우 자동으로 할당 (동일한 역할)
    - Boolean: true, false는 자동 형변환 규칙에 따라 true 또는 false로 변환
    ![image](https://user-images.githubusercontent.com/118239192/224943217-4d771bad-40c7-42bf-8579-ab2e7f76e018.png)

    ```html
    <!-- Template-literal -->
    <script>
        const age=31
        const message=`iu의 나이는 ${age}`
    </script>
    ```

3. 연산자
- 할당 연산자 (오른쪽에 있는 평가 결과를 왼쪽 피연산자에 할당)
    - a+=b (a=a+b)
    - a-=b (a=a-b)
    - a++ (a=a+1)
    - a-- (a=a-1)
- 비교 연산자 (< , >)
- 동등 연산자 (`==`)- 두 연산자가 같은 값으로 비교되는지 비교 후 boolean 판단  (암묵적 타입 변환으로 판단, 예상치 못한 결과 발생 가능)  => `특별한 경우 제외하고 사용 x`
- 일치 연산자(`===`) - 두 피연산자의 값과 타입이 모두 같은 경우 True 반환
- 논리 연산자 
     - and (&&) 
     - or (||)
     - not(!)
    
4. 조건문
- 조건 표현식의 결과를 boolean 타입으로 변환 후 참/거짓 판단 (`중괄호 사용`,`else if` 사용)
```html
<script>
if (name='iu'){
console.log('라일락')
}else if (name='taeyeon'){
    console.log('gravity')
}
</script>
```

5. 반복문
- while 문: 조건문이 참이기만 하면 문장 계속 수행
- for 문 :특정한 조건이 거짓으로 판별될 때까지 반복- for ([초기문];[조건문];[증감문])
```html
<script>
for(let i=0;i<5;i++){
    console.log(i)
} //0,1,2,3,4
// 1. 반복문 진입 후 변수 i 선언
// 2. 조건문 평가 후코드 블럭 실행
// 3. 코드블록 실행 후 i 증가
</script>
```
- for in 문 : 객체 속성 순회할 때 사용  (순서에 따라 인덱스 반환을 보장하지 않는다)
- for of 문 : 반복 가능한 객체(배열,문자열) 순회할 때 사용
```html
<script>
const arr=[3,5,7]
for (const i in arr){
    console.log(i)  //0 1 2
}
for (const i of arr){
    console.log(i) //3 5 7
}
</script>
```

6. 참고사항
- 세미콜론은 선택적으로 삽입 가능 (사용하지 않을경우 ASI가 자동으로 삽입)
- var : 재할당 ,재선언 가능한 변수 호이스팅되는 특성 => let,const 사용 권장 
- 함수 스코프: 함수의 중괄호 내부 (함수 바깥에서 접근 불가)
- 호이스팅: 변수 선언 이전에 참조하는 현상 (변수 선언 이전일 경우 undefined 반환)  ,자바스크립트가 실제 실행시 변수들이 최상단으로 올라가므로 `undefined로 값이 초기화 되는 문제`
- for문 :const 사용시 에러 발생/ for in , for of 문 : const를 사용해도 에러가 발생 x
- NAN 반환하는 경우 
     - 숫자로 읽을 수 없는 경우
     - 결과가 허수인 수학 계산식
     - 피연산자가 NAN
     - 정의할 수 없는 계산 식
     - 문자열을 포함하면서 덧셈이 아닌 계산식 ('A'/3)