# Introduction of Web page
- World Wide Web :인터넷으로 연결된 거대한 정보 공간
- Web site : 여러개의 Web page가 모인 것
- Web page: HTML, CSS,Javascript 등의 웹 기술을 통해 만든 인터넷 문서
    - HTML: 웹 페이지의 `structure`
    - CSS : 웹 페이지 `styiling` (디자인)
    - Javascript: 웹 페이지의 Behaviour(웹 페이지 행동방식)
- 웹 페이지들이 모여서 웹 사이트를 만들고, Web은 웹 페이지, 웹 사이트 모두를 포함하는 상위 개념이다

## Introduction To HTML
- HTML (Hyper Text Markup Language):웹 페이지 의미와 구조를 정의하는 언어
    - Hyper Text 란? 참조를 통해서 사용자가 한 문서에서 `다른 문서로 접근` 가능 
    - Markup Language란? 태그 등을 이용해 문서나 데이터의 구조를 명시하는 언어이다


## Structure of HTML
- HTML ELEMENT는 여는 태그, content,닫는 태그(`/`포함)로 구성된다.
- 닫는 태그가 없는 태그도 존재핟나 (굳이 content가 필요하지 않은 ELEMENT)
- HTML Attributes
    - 규칙 
        - 요소 이름 바로 다음에 오는 속성은 공백 필요
        - 하나 이상의 속성들이 있는 경우 속성 사이 공백으로구분
        - 속성값은 따옴표로 열고 닫아야 한다
```html
<p class="dlwlrma">Content</p>
```
- HTML 문서의 기본 구조 
    - `<!DOCTYPE HTML>`:문서가 HTML 문서라는 것을 나타낸다
    -<html></html> :전체 페이지의 콘텐츠를 포함한다
    -<title></title>:브라우저 탭 및 즐겨찾기시 제목으로 사용한다
    -<head></head>: html 문서 관련된 설정,설명 사용자는 볼 수 없다
    -<body></body>:페이지에 표시되는 모든 콘텐츠, 사용자가 보는 내용이다
```html
<!-- vscode에서 !를 통해 기본 구조 한번에 불러올 수 있다 -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>
```
### HTML Test Structure
- Heading(상위 제목) : h1~h6
- Paragraphs(단락): p
- Lists:ol(ordered list),ul(unorderedlist),li
- Emphasis: em
- Importance: strong

## Introduction to CSS
- CSS(Cascading Style Sheet): 웹 페이지 디자인과 레이아웃 구성하는 언어 
- CSS 구문은 선택자,선언으로 이루어져있다
```html
<style>
h1{color:'blue';font-size:15px;} 
</style>
<!-- h1이 선택자, color:blue가 선언문 -->
```

### CSS 적용 방법
1. 인라인(Inline) 스타일
- body에 있는 content가 있는 구문 안에 직접 구현
```html
<body>
<h1 style="color:blue;">인라인</h1>
</body>
```
2. 내부(Internal)스타일
- head 에 있는 설정에 스타일을 직접 설정
```html
<head>
    <style>
    h1{color:'blue'}
    </style>
</head>
```
3. 외부(External) 스타일
- 별도의 css파일 생성후 불러온다
```html
<!-- style.css -->
h1{color:blue}
<!-- 이를 html파일에서 불러온다 -->
<head>
    <link rel="stylesheet" href="style.css">
</head>
```

관리 측면에서는 외부 스타일이 용이하고, 코드 작성 및 편의에는 내부스타일이 용이하다

### CSS Selectors
- HTML 요소를 선택하여 스타일 적용할 수 있게 한다 
- 기본 선택자
    - 전체(*) 선택자
    - 요소(tag) 선택자
    - 클래스(class) 선택자
    - 아이디(id) 선택자
    - 속성(attr) 선택자
- 결합자
    - 자손 결합자 (" "(space))
    - 자식 결합자 (>)

### CSS SELECTOR의 특징
- 요소 선택자: 지정한 모든 태그를 선택한다
- class 선택자: 주어진 클래스 속성 가진 모든 요소를 선택한다
- id 선택자: 주어진 아이디 속성을 가진 요소 선택(주어진 id 가진 요소 1개 있어야함) 
2개 있어도 코드가 실행되지만 1개인 것이 원칙
- 자손 선택자:첫 번째 요소의 자손 요소들을 선택한다
- 자식 선택자:첫 번째 요소의 직계 자식만 선택
```html
    <style>
    *{color:red}
    h2{color:orange}
    /*요소가 h3,h4*/
    h3,h4{color:blue}
    /*class가 green*/
    .green{color:green}
    /* id가 puple 선택자 */
    #purple{color:purple}
   /*위에 클래스가 그린이면서 자식이 span인 애를 fontsize 50픽셀로 바꾸고싶다! */
    .green > span{font-size:50px;} 
    /* 자손선택자 클래스 그린의 모든 자손 리스트의 색깔을 바꿔준다 */
    .green li{color:brown;}
    </style> 
```

### Cascade & Specificity
- 동일한 요소에 적용 가능한 Stlye 작성 시 어떤 규칙이 적용될 것인가?
- Cascade(계단식): 동일한 우선순위 일 경우 CSS 마지막 규칙이 적용된다
- Specificity(우선순위):선택자 별로 높은 우선순위에 따라 규칙이 적용된다
    - Importance : `!important` 사용시 최우선 순위 (사용하지 않는 것 권장)
    - 우선순위: 인라인스타일>id 선택자>class 선태자 >요소 선택자
    - 위 우선순위를 다 확인 후 소스코드 순서(계단식)

### 상속
- CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속한다
- 상속되는 속성: Text 관련 요소(font,color,text_align) 등..
- 상속되지 않는 속성: Box model 관련 요소(width,height...), Position 관련 요소(top/right/bottom...)

### HTML, CSS 참고사항
- HTML요소 이름 소문자 사용 권장
- HTML 속성 따옴표는 큰 따옴표 권장
- CSS 인라인 스타일은 코드 유지,보수 힘들기 때문에 권장하지 않는다
- 속성은 Class 사용을 하되, 한 번만 나오는 스타일은 id 사용 고려