# JavaScript Function
- Function: 참조 자료형, 모든 함수는 Function Object
- 함수는 이름, 매개변수,statement로 구성되어있다 
- 함수는 선언식과 표현식으로 정의내릴 수 있다
    - 선언식: 함수 이름을 선언후 함수 정의
    - 표현식: 익명 함수 이용, 호이스팅 되지 않으므로 코드에 나타기 전에 미리 사용 가능  (사용 권장)
```html
<script>
    // 선언식
function add (num1,num2){
    return num1+num2
}
// 표현식
const add2=function(num1,num2){
    return num1+num2
}
```
- 함수의 매개변수 => 값이 없거나 undefined 전달될 경우 이름 붙은 매개변수를 기본값으로 초기화한다
```html
<script>
const hello=function(name='iu'){
    return `hi ${name}`
} // hi iu 
```
- 매개변수와 인자개수가 불일치 할 경우 
    - 매개변수 개수 < 인자개수 : 인자개수만큼만 사용 (1,2,3)=> (1,2)
    - 매개변수 개수 > 인자개수: : 매개변수 개수만큼 사용 후 남은 개수는 undefined
    - 나머지 매개변수 `Rest parameter` : 무수한 수의 인자를 배열로 허용  (`...`으로 표현)
```html
<script>
cosnst reFunc=function(param1,param2,parma3,...restParams){
    return [param1,parmm2,restparams]
}
</script>
```

- ArrowFucntion (함수 식 간결히 표현)
    - 1. fucntion 키워드 제거 후 매개변수와 중괄호 사이 화살표 (`=>`)작성
    - 2. 함수의 매개변수 하나라면 매개변수의 () 제거가능
    - 3. 함수 본문 표현식 한줄이라면 {}, return 제거 가능


# JavaScript Object
- 키로 구분된 데이터 집합 (파이썬에서의 딕셔너리 형태)
- 중괄호 이용해 구성, key:value 쌍 형태 (property 속성)
- key는 문자형 ,value는 모든 자료형 허용
```html
<script>
const singer={
    name:'iu',
    age:'31',
    'lilac':true
}
// 속성 조회
console.log(singer.name)
// 속성 추가
singer.now=drama
// 속성 수정
singer.age=32
//삭제
delete.singer.age
// 존재 여부 확인
console.log(age in singer) //true
console.log(movie in singer)// false
</script>
```
- 계산된 property: 키를 `[]` 대괄호로 묶어서 가변적인 변수값으로 사용할 수 있다 (`prompt`이용시 input받아 설정)

## JavaScript Object -객체와 함수
- Method: 객체 속성에 정의된 함수  (`object.method()`)
- `this`키워드를 사용하면 객체에 대해서 특정 작업 수행이 가능하다
- `this`keyword= 함수나 매서드를 호출한 객체를 가리키는 키워드
    - 단순 호출시 :전역객체 
    - 메서드 호출시: 메서드를 호출한 객체
```html
<script>
const myF=function(){
    return this
}
console.log(myF()) // window (document)의 전역객체

const myO={
    data:1,
    myOf:fucntion(){
        return this
    }
}
console.log(myO.myOf()) // myO 
```
- nested 함수(함수 중첩)시 this가 원하는 객체를 가리키지 못하고 전역 객체를 가리킬 수 있다 => 화살표 함수는 자신의 this를 가리키지 않기 때문에 외부함수에서 this를 가져와서 문제 해결 가능 

- Object.keys/ Object.values 로 key,value 모음 확인 가능
```html
<script>
console.log(Object.keys(singer))
console.log(Object.values(singer))
</script>
```

## Javascirpt Object 참고사항
- JS에서 this는 호출되는 방식에 따라 결정되는 객체,함수 호출 전까지 값 할당 x, 호출시에 결정 (동적이다)
- JSON(JavaScript Object Notation) 
    - key-value 형태
    - JavasScript에서 Json 사용하려면 Object로 변환 필요
    - Object -> json :`Json.stringify` 사용
    - Json -> Object :`Json.parse` 사용

# JavaScript Array
-순서가 있는 데이터 집합을 저장하는 자료구조
- 대괄호 이용해 작성 , length 사용해 요소 개수 파악 가능 (파이썬 리스트와 유사한 형태)
- 배열의 마지막 요소 역시 객체와 마찬가지로 쉼표로 끝날 수 있다 
- 배열과 메서드
![image](https://user-images.githubusercontent.com/118239192/225290757-026c87b3-4b77-46f9-9c9b-cba6626605a3.png)

- forEach와 map은 콜백함수 => 다른 함수에 인자로 전달되는 함수 
- 콜백함수는 재사용성 +비동기적 처리(settimeout 함수등 사용시) 측면에서 유용하다