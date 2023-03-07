# Bootstrap Grid System
- 웹 페이지 레이아웃을 조정할 때 12개의 컬럼으로 구성된 시스템
- 모바일,태블릿,데스크탑 등 다양한 기기에서 적절하게 표시할 수 있다.

## Grid System Basis
-  가장 기본그리드 박스를 `container` class로 설정한다 
- 12개의 column이 들어가는 각 줄을 `row` class로 설정한다
- `col-n` class 를 통해 설정하여 12개의 컬럼중 차지하는 비율을 설정한다
- `offset` class를 통해 12개의 컬럼 중 건너뛰는 부분을 설정한다
- Gutter - row class에 `gx-n(수평), gy-n(수직),g-n(수직수평)` 을 통해 Padding을 설정한다

- 예시 코드
```html
<body>
<!-- 기본 container -->
<div class="container">
    <!--row 설정  -->
    <div class="row">
        <!--  3개 차지는 grid 구성-->
        <div class="col-3">~~</div> 
        <div class="col-3">~~</div> 
        <!-- 3개 건너 뛰는 grid 구성 -->
        <div class="col-3 offset-3">~~</div> 
    <!-- gutter 수평수직 3씩 padding 설정 -->
    <div class="row g-3">
        <div class="col-6">~~</div>
        <div class="col-6">~~</div>
        <div class="col-6">~~</div>
        <div class="col-6">~~</div>
    </div>
</div>
<body>
```