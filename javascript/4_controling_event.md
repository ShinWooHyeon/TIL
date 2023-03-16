# JavaScript Event
- Event:무언가가 일어난 신호, 사건
- 모든 DOM요소는 event를 처리할 수 있다 
- `event handler`: 이벤트 발생 시 실행되는 함수    
    - .addEventListener() 
        - 대표적인 이벤트 핸들러 
        - 특정 이벤트 DOM 요소가 `수신할 때 마다` 콜백 함수 호출 
        - EventTarget.addEventlistener(type,handler) 
        - EventTarget은 DOM 요소, type은 이벤트 종류, handler는 콜백함수 이다
    

## Event Hadnler Case
- Click
```html
<script>
//Click 활용더하기 빼기 버튼 만들기
  const btn1=document.querySelector('#plus')
  let counterNumber = 0
  const spanTag=document.querySelector('#result') 
  btn1.addEventListener('click',()=>{ // type= click
    counterNumber+=1  // 클릭할 때마다 숫자 증가
    spanTag.textContent=counterNumber //증가된 숫자를 내용에 삽입
  })

  const btn2=document.querySelector('#minus')
  btn2.addEventListener('click',()=>{
    counterNumber-=1
    spanTag.textContent=counterNumber
  })
</script>
```
- Input 
```html
<script>
  //input과 clcik 활용한 입력한 만큼 숫자를 더하거나 빼기
  const inputTag = document.querySelector('#number')
  const spanTag=document.querySelector('#result')
  const btn1=document.querySelector('#plus')
  let counterNumber=0
  let num=0
  inputTag.addEventListener('input', (event) => {
    num=Number(event.target.value)  // input을 받을때 마다 num저장하고
  })                                    
  // +버튼 클릭할 때마다 저장한 num을 더한다
  btn1.addEventListener('click',()=>{
    counterNumber+=num
    spanTag.textContent=counterNumber  
  })

   // -버튼 클릭할 때 마다 저장한 num을 뺀다
  const btn2=document.querySelector('#minus')
  btn2.addEventListener('click',()=>{
    counterNumber-=num
    spanTag.textContent=counterNumber
  })
</script>
```
- preventDefault() -현재 Event의 기본 동작을 중단한다
```html
  <script>
    const h1Tag = document.querySelector('h1')
    // copy가 일어날 경우 
    h1Tag.addEventListener('copy', (event) => {
      console.log(event)
      event.preventDefault() //동작을 중지하고
      alert('복사불가.')   //alert함수 통해 경고표시를 실행할 수 있다.
    })
  </script>
  ```

 - lodash - JavaSciprt 유틸리티 라이브러리, array나 object등의자료구조 다룰때 사용하는 간편한 함수를 제공

