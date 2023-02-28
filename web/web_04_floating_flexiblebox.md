# Floating CSS
- CSS Float: 요소를 띄워서 텍스트 및 인라인 요소가 그 주위를 감싸도록 배치한다(신문이 대표적인 예시)
- `float: left, float : right` 코드를 통해서 이용
- 실제로는 잘 사용하지 안혹 `Flexiblebox` 를 중점적으로 사용한다 

# Flexbile box for CSS
- CSS Flexbox: 요소를 행과 열 형태로 배치하는 레이아웃방식
- Flexbox
    - main axis(주축):flex item이 배치되는 기본 , main start 시작~ main end 방향
    - cross axis(교차축):`main axis에 수직`인 축 ,cross start 시작~ cross end 방향
    - Flex container:`display:flex` or display:inline-flex 가 설정된 부모요소 (`1차 자식`요소들이 flex item이 된다)
    - Flex item: Flex container 내부에 레이아웃이 되는 항목

## Flexible box Layout 
- Flexbox 속성
![image](https://user-images.githubusercontent.com/118239192/221825295-0bcc78a6-1946-479b-8f4f-508795d4a822.png)

1. Flex contatiner 지정 :`display:flex`
```html
<style>
    .contatiner{display:flex;}
/* 행으로 나열, 주축의 시작선에서 시작, 교차축을 채우는 방식으로 나열 */
```
2. Flex direction 지정: flex item이 나열되는 방향, column: 주축변경, reverse: 시작선 끝선 변경
```html
<style>
    .contatiner{display:flex;
    flex-direction:row;
 /* flex-direction: column; */
      /* flex-direction: row-reverse; */
      /* flex-direction: column-reverse; */}
```

3. flex-wrap:flex item이 flex contatiner 한 행에 못 들어갈 경우 다른행 배치 결정
```html
<style>
    .contatiner{display:flex;
    flex-wrap:nowrap;}
 /* flex-wrap:wrap; */
</style>
```

4. justify-content: 주축 기준 flex item 공간 분배
```html
<style>
    .contatiner{display:flex;
    justify-content:flex-start;
      /* justify-content: center; */
      /* justify-content: flex-end; */}
</style>
```

5. align-content: 교차축 기준 flex item 공간 분배 (`flex-wrap이 wrap 혹은 wrap-reverse인 경우에만 적용 된다 )
```html
<style>
    .contatiner{display:flex;
    align-content:flex-start;
      /* align-content: center; */
      /* align-content: flex-end; */}
</style>
```

6. align-items: 교차축 따라 flex item 행을 정렬한다 
```html
<style>
    .contatiner{display:flex;
    align-items:flex-start;
      /* align-items: center; */
      /* align-items: flex-end; */}
</style>
```

7. align-self: 교차 축 따라 `개별` flex item 정렬
```html
<style>
.item1{align-self:center
/*flex-end,flex-start*/}
</style>
```

- 정리
    - 배치설정: flex-direction/flex-wrap
    - 공간분배: justify-content/align-content
    - 정렬: align-items/align-self
    - `Content는 여려행, items는 행, self는 개별 1개 item`
    - justify: 주축, align: 교차축

8. flex-grow: 남는 행 여백을 비율에 따라 flex item에 분배한다 (반대는 flex-shrink 남는부분 비율조 주는 것)
```html
<style>
.item1{
    flex-grow:1
}
.item2
{flex-grow:2}
/*flex-grow는 최종 비율이 아닌 남는 여백을 비율대로 나누어주는것이다*/
```
9. flex-basis: flex item의 초기 크기 값을 지정 (flex-bias와 width 동시에 적용 시 flex-bias 우선적용)
```html
<style>
.item1{flex-basis:300px;}
```
- 반응형 레이아웃: flex-wrap을 이용해서 창이 줄어들 때 번하게 하고 flex-basis설정해서 조정이 가능하다
( flex-grow를 이용하면 여백을 제거해서 효과적인반응형 레이아웃 제작 가능)