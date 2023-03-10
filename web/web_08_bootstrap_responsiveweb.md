# Responsive Web Design
- 디바이스 종류나 화면 크기등에 상관없이 일관된 레이아웃 제공하는 기술
- Bootstrap은 12개의 column, 6개의 breakpoint를 사용하여 반응형 웹 디자인을 구현한다 

# Breakpoints
- 다양한 화면 크기에서 적절하게 배치하기 위한 `분기점`
- 설정된 최대 너비 값 이상으로 바뀔 경우 grid system 동작이 바뀐다
- grid system breakpoint는 다음과 같다
![image](https://user-images.githubusercontent.com/118239192/223680038-0dbe1b2c-0860-4b88-83a5-043ce985b496.png)
- 예시 코드
```html
<body>
<div class="container">
<div class="row">
    <div class="col-12 col-sm-6 col-md-2 col-lg-3 col-xl-4">
    <div class="box">col </div>
    </div>
        <div class="col-12 col-sm-6 col-md-8 col-lg-3 col-xl-4">
    <div class="box">col </div>
    </div>
        <div class="col-12 col-sm-6 col-md-2 col-lg-3 col-xl-4">
    <div class="box">col </div>
    </div>
        <div class="col-12 col-sm-6 col-md-12 col-lg-3 col-xl-12">
    <div class="box">col </div>
<!-- XS에서는 12차지하므로 4줄/ SM에서는 2개씩 2줄 -->
<!-- md에서는 2,8,2로/12로 두줄 lg는 다시 한줄 xl는 4,4,4/12로 두줄 -->
    </div>
<div>
</div>
```
- row cols를 통해서 행당 표시할 열(카드)수를 제어할 수 있다 (`row-cols-3 은 3개만 표시`)