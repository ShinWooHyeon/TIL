# 파일의 입출력
- 파일 입력
```python
open(file,mode='r',encoding=None)
# mode는 아래 사진과 같이 여러 종류가 있다
# 인코딩방식은 UTF-8을 일반적으로 활용한다
```
<img width="468" alt="open 모드" src="https://user-images.githubusercontent.com/118239192/210994738-818adc2a-1769-4610-9e5c-20adc69b95ae.png">

- with 키워드를 사용해서도 입출력 가능, with 키워드 사용x면 f.close() 반드시 호출 (with 키워드는 with 블럭안에서만 열려있다고 생각~)
```python
with open ('IU.txt','r') as f
```

# Json
- Json은 자바스크립트 객체 표기법, 개발환경에서 많이 사용되는 데이터 양식
- 문자(텍스트) 기반 데이터 포멧으로 다수의 환경에서 활용 가능
- json 파일의 활용 예시는 다음과 같다

<img width="538" alt="json 1" src="https://user-images.githubusercontent.com/118239192/210996908-f5549c79-aa18-403f-a969-b1e4eff6da51.png">

<img width="398" alt="json 2" src="https://user-images.githubusercontent.com/118239192/210996920-d49ab982-dd34-4036-aa6f-52fb83a0dbdf.png">

- pprint를 사용하면 깔끔하게 출력할 수 있다!