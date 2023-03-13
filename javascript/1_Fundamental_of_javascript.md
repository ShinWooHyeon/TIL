# Javascript History
- Internet Explorer와 경쟁할 브라우저 개발 중 동적인 기능 추가 위해서 `javascript` 개발 
- 많은 회사들이 자체적으로 Javascript 업데이트, 브라우저 마다 코드가 다르게 동작
- IE의 지배속 2008년 구글의 `Chrome` 브라우저가 점유율 1위를 3년만에 차지
- 웹 표준 발전,웹 애플리케이션 대중화에 큰 역할을 함
- Javascript는 현재 웹 페이지 동작 기능 구현 뿐만 아니라 다양한 라이브러리에서 필수적인 언어로 자리잡음
- ECMAScript : 국제기구에서 정의한 표준화 된 스크립트 프로그래밍 언어 ( Javascript 의 구현 언어 중 하나이다)

# Javascript 
- JavaScrpit의 실행 환경은 HTML Script 태그, js 확장자 파일, 브라우저의 console이 있다
```html
<body>
<script>
console.log()
</script>
</body>
```

# DOM (Document Object Model)
- 웹 페이지를 구조화 된 객체로 제공하며 `프로그래밍 언어가 웹 페이지 사용` 하도록 연결해준다
- 브라우저는 HTML 문서를 해석하여 DOM tree 라는 객체로 구조화한다
- DOM에서 모든 요소,속성,텍스트는 하나의 객체 모두 `document` 객체의 자식이다 
- 웹 페이지 조작을 위해선 `1.선택 /탐색 `  그리고 `2.선택 요소 조작`이 이루어져야 한다. 

- document Object는 웹 페이지 객체, 모든 객체요소를 포함한다

## DOM Query

1. 선택
- 요소 하나를 선택하는 기능 `document.querySelector()` ,만족하는 객체 없으면 null 반환
- 요소 여러개를 선택하는 기능 `document.querySelectorAll()`, 만족하는 객체 없으면 Nodelist 반환

2. 조작
- 속성 조작
    - 클래스 속성 조작 `classList` = element.classList.add|remove()
    - 일반 속성 조작 
        - .getAttribute():속성 조회
        - .setAttribute():속성 설정,수정
        - .removeAttribute():속성 삭제
    - 콘텐츠 조작 : `textcontent` 이용해서 변수 지정 후 수정

- 요소 조작
     - .createElement: 요소 생성
     - .appendChild: 요소 추가 (이미 문서에 존재하는 요소를 다른 요소 자식으로 삽입시 위치가 이동)
     - .removeChild: 요소 삭제
- Style 속성 조작 - `.style.~` 로 조작
    