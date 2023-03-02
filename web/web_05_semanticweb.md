# Semantic web
- 웹 데이터를 의미론적으로 표현하고 연결하는 개념
- 시각적인 의미가 아닌 목적,역할을 의미한다.

## Semantics -HTML
-  기본적인 모양,기능 뿐만 아니라 의미를 가지는 HTML 요소
- ex. `<h1>` 과 `<font-size:32px>` 동일한 모양,기능이지만 웹 서칭시 나오게 되는 요소는 헤더이다
- 검색엔진과 웹 페이지 콘텐츠의 높은 이해를 돕는다 
- 주요 semantic element (div와 기능은 같지만 의미가 다르다!)
    - header
    - nav
    - main
    - article
    - section
    - aside
    - footer

## OOCSS-객체 지향적 접근법을 이용한 CSS 
- 공통 되는 요소들을 하나의 객체로 뽑고, 다른 요소들만 새로운 객체를 만든다
- ex. 버튼1 버튼2 서로 다룬 두 객체를 만드는게 아닌 공통된 버튼요소를 만들고, 색깔과 같은 객체만 따로 만든다.

## BEM(Block Element Modifier)- 블록,요소,수정자를 사용 클래스 구조화
- Block: 문단 전체 요소를 담고 있는 컨테이너, 재사용을 위해 padding과 margin을 적용x
- Element: blcok이 포함하고 있는 요소
- Modifier: block또는 element의 속성
```html
<style>
.block{} 
.block__element{}/*슬래시 2개*/
.block__element--modifier{} /*하이픈 2개*/
```

- Semantics의 이점
    - 검색 엔진의 웹사이트 분석 용이
    - 시각 장애 사용자의 웹페이지 사용에 도움
    - 의미를 분명하게 전달할 수 있음 => 개발자 간의 협력 향상