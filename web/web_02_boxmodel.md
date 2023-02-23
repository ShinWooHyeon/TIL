# BOX Model
- CSS BOX Model : 모든 HTML 요소를 박스(사각형)로 표현하는 것
- 구성요소
    - Margin: 박스와 다른 요소 사이의 공백, 가장 바깥 쪽 영역이다
    - Border: 콘텐츠와 패딩을 감싸는 테두리 영역
    - Content: 콘텐츠가 표시되는 영역
    - Padding: 콘텐츠 주위에 위치하는 공백영역
- BOX의 속성
    - 요소(content)의 width와 height를 지정할 수 있다
    - boxsizing : box 전체의 사이즈를 한 꺼번에 설정하고 싶다(border,padding 등... 합으로 고려하는 것은 불편=>`box-sizing :border-box` 
```html
<head>
    <style>
        .box{box 크기~}
        .border-box{box-sizing:border-box}
    </style>
<body>
    <div class="box border-box">border-box </div>
<!-- 전체 박스 크기를 결정해준다 -->
```

## BOX TYPE
- Blcok 과 inline 타입이 있다
- BLOCK Directin의 Normal flow는 수직(하단)방향, Inline은 수평(우측)방향이다
- Block Type 특징  
    - 항상 새로운 행 (수직방향이므로)
    - width와 height를 통해서 너비와 높이를 지정할 수 있다 
    - width를 지정하지 않을 경우 사용 가능한 모든 너비를 `100%` 차지한다
    - 대표적인 태그 : h1~6, p , div
- Inline Type 특징
    - 새로운 행으로 나눠지지 않는다
    - width,height 속성 지정 불가
    - 수직방향 padding,margin,border 적용 x `수평방향은 적용 가능`
    - 대표적인 태그: a, img, span

## Box Model Additional..
- Shorthand : border,margin,padding의 여러 속성들을 한 꺼번어 설정 가능
```html
<style>
.box{border: 1px}  /* 순서 상관 x, width,style,color 한번에 설정 가능*/
.box1{margin: 10px 20px 30px 40px;} /*4개면 상우하좌 순서*/
.box2{padding: 10px 20px 30px 40px;}
/*3개 일경우 상,좌우,하*/
/*2개일경우 상하,좌우*/
/*1개일경우 상하좌우 모두 동일*/
</style>
```
- Inline-block: Inline과 block 사이에 중간 지점 제공하는 display
    - 요소가 줄 바꿈은 되지 않고 `높이 너비 설정이 가능`하다

- Margin Collapsing(마진상쇄): 두 block 타입 요소의 margin top과 margin bottom이 만날 경우 => 큰 Margin으로 상쇄된다 

